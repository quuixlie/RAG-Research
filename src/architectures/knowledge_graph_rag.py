from pydantic import BaseModel
import json
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain.schema import Document
import pymupdf
from torch.autograd import graph
from src.cross_encoder import CrossEncoder
from src.architectures.__rag_architecture import RAGArchitecture
from src.embedder import LangchainEmbedderWrapper,Embedder, LocalEmbedder
from src.tokenizer import Tokenizer
from src.utils.document_parser import parse_to_markdown
from src.llm import LLM,LangchainLLMWrapper, OpenAILLM
from langchain_neo4j import Neo4jVector,Neo4jGraph
from langchain_neo4j.graphs.graph_document import GraphDocument
from langchain_neo4j.vectorstores.neo4j_vector import remove_lucene_chars
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

from typing import List


class Relation(BaseModel):
    text: str
    subject:str
    subject_type:str
    object:str
    object_type:str
    relation:str


class KGraphRAG(RAGArchitecture):
    """
    RAG implementation with the usage of Knowledge Graphs and Vector embeddings

    It uses neo4j as the graph and vector database.
    Graph representation of the data can be viewed at localhost:7474 (if neo4j service is running)
    """

    def __init__(self,llm:LLM,tokenizer:Tokenizer,embedder:Embedder,cross_encoder:CrossEncoder,graph_top_k:int=15, vector_top_k:int = 5,graph_max_retrieved:int=50,vector_max_retrieved:int = 20,neo4j_uri="bolt://localhost:7678",neo4j_user="neo4j",neo4j_password="your_password"):
        """
        Args: 
            llm: LLM Used for graph generation and answer.
            tokenizer: tokenizer used to split documents into chunks
            embedder: embeddings used for vector db
            graph_top_k: Number of relations after reranking
            graph_max_retrieved: Number of relations extracted from the database
            vector_top_k: Number of text context after reranking
            vector_max_retrieved: Number of text context retrieved from the database
        """
        self.llm = llm
        self.tokenizer = tokenizer
        self.embedder = embedder
        self.cross_encoder = cross_encoder
        self.vector_top_k = vector_top_k
        self.vecotr_max_retrieved = vector_max_retrieved
        self.graph_top_k = graph_top_k
        self.graph_max_retrieved = graph_max_retrieved

        self.neo4j_conn_data = {'url':neo4j_uri,'username':neo4j_user,"password":neo4j_password}

        self.db = Neo4jGraph(url=neo4j_uri,username=neo4j_user,password=neo4j_password)
        self.vector_index = Neo4jVector(embedding=LangchainEmbedderWrapper(embedder=embedder),url=neo4j_uri,username=neo4j_user,password=neo4j_password)
        pass

    def generate_relations(self,chunks:list[str]) ->  List[GraphDocument]: #list[Relation]:
        """
        Generates relations as triplets in the format (subject,relation,object)
        """
        ## Langchain version
        llm_wrapper = LangchainLLMWrapper(llm=self.llm)
        graph_transformer = LLMGraphTransformer(llm=llm_wrapper)
        docs = [Document(page_content=c) for c in chunks]
        graph_documents = graph_transformer.convert_to_graph_documents(docs)
        return graph_documents

    
        ## My own version - rest of my own graphrag is not finished so this is notuseful for now

        system_prompt = """
You are an intelligent system designed to extract structured knowledge in the form of relations for use in a knowledge graph.
Your task is to analyze the provided input text and return a list of factual triplets, each consisting of:
(subject, predicate, object).
Extract only statements explicitly present or directly implied in the text. Not speculations beyond the text.
Use full unambiguous entity names(e.g. "Marie Curie" and not "Marie").
If the same person is mentioned multiple times with different pronouns or names make sure you give the node a full name (e.g. "Marie Curie", "She", "Her's", "Marie" all should be "Marie Curie" if the context is about her).
Do not repeat the same triplet.
Predicate style: Use clear, snake_case relations (e.g. born_in, wokrs_at, has_trait)
ber).
For each relation you should output a JSON object that will contain these fields:
1. "text" - text fragment used to create a relation
2. "subject" - The subject of relation
3. "subject_type" - The type of the subject (e.g. Person)
4. "object" - The object of relation
5. "object_type" - The type of the object (e.g. Person)
6. "relation" - the relation
Your response should be a list of these JSON object.
Always respond with pure JSON data - not additional formatting or commentary.
Always make sure you are following these given rules as accurately as possible.
"""

        previous_system_prompt = self.llm.system_prompt
        self.llm.system_prompt = system_prompt

        relations = []

        # for every chunk we ask a LLM to generate the relations/predicates
        for chunk in chunks:
            prompt = "Make sure you are strictly following the rules and comply to the given response format.\n" + "The text that you should generate relations for is starting from the next line\n" + chunk
            response_json = self.llm.generate(prompt)

            print("============= OUTPUT =============")
            print(response_json)
            print("============= ===== =============")

            relation_list = json.loads(response_json)

            relations.extend([Relation.model_validate(x) for x in relation_list])


        self.llm.system_prompt = previous_system_prompt

        return relations

    def process_document(self, conversation_id: int, document: pymupdf.Document) -> None:
        markdown = parse_to_markdown(document)
        chunks = self.tokenizer.tokenize(markdown)

        relations = self.generate_relations(chunks)

        self.db.add_graph_documents(
            graph_documents=relations,
            baseEntityLabel=True,
            include_source=True
        )
        self.vector_index = Neo4jVector.from_existing_graph(
            embedding=LangchainEmbedderWrapper(embedder=self.embedder),
            search_type="hybrid",
            node_label="Document",
            text_node_properties=["text"],
            embedding_node_property="embedding",
            **self.neo4j_conn_data
        )
        return None


    def process_query(self, conversation_id: int, query: str) -> dict:
        # Getting data from the database
        graph_raw = self._graph_retriever(query)
        vector_raw = self._vector_retriever(query)


        # Reranking
        graph_ctx = self._rerank(query,graph_raw,self.graph_top_k)
        vector_ctx = self._rerank(query,vector_raw,self.vector_top_k)

        print(len(graph_raw), len(set(graph_raw)),len(graph_ctx),len(set(graph_ctx)))

        prompt =self.create_prompt(query,graph_ctx,vector_ctx)

        sys = self.llm.system_prompt
        self.llm.system_prompt = "You are a Helpful assistant, try to answer the given question. You are given a list of relations in format subject -> RELATION -> object. and some text contexts."

        answer = self.llm.generate(prompt)

        

        self.llm.system_prompt = sys

        return {
            "query":query,
            "answer":answer,
            "graph_context":graph_ctx,
            "vector_context":vector_ctx
        }

    def create_prompt(self,query:str,graph_contexts:List[str],vector_contexts:List[str]) -> str:
        return f"=ENTITY_RELATIONS=\n{"\n".join(graph_contexts)}\n=TEXTS=\n{"\n".join(vector_contexts)}\n=QUESTION=\n{query}"

    def _rerank(self, query: str, contexts: List[str], k: int) -> List[str]:
        if not contexts:
            return []
        q_emb = self.embedder.embed(query)  
        c_embs = self.embedder.embed_fragments(contexts)
        sims = cosine_similarity([q_emb], c_embs)[0]  
        idx_sorted = np.argsort(sims)[::-1][:k]
        print(idx_sorted)
        ## TODO :: Cos tu nie gra po rerankinug sa duplikaty
        ## TODO :: Cos tu nie gra po rerankinug sa duplikaty
        ## TODO :: Cos tu nie gra po rerankinug sa duplikaty
        ## TODO :: Cos tu nie gra po rerankinug sa duplikaty
        ## TODO :: Cos tu nie gra po rerankinug sa duplikaty
        return [contexts[i] for i in idx_sorted]

    def _vector_retriever(self,query:str) -> List[str]:
        return [el.page_content for el in self.vector_index.similarity_search(query,k=self.vecotr_max_retrieved)]

    def _graph_retriever(self,query:str) -> List[str]:
        entities = self._extract_entities(query)

        self.db.query("CREATE FULLTEXT INDEX entity IF NOT EXISTS FOR (e:__Entity__) ON EACH [e.id]")

        # List of relations
        results: List[str] = []

        for entity in entities:
            r = self.db.query(
                f"""CALL db.index.fulltext.queryNodes('entity', $query, 
                    {{limit:2}})
                    YIELD node,score
                    CALL () {{
                      MATCH (node)-[r:!MENTIONS]->(neighbor)
                      RETURN node.id + ' - ' + type(r) + ' -> ' + neighbor.id AS 
                      output
                      UNION
                      MATCH (node)<-[r:!MENTIONS]-(neighbor)
                      RETURN neighbor.id + ' - ' + type(r) + ' -> ' +  node.id AS 
                      output
                    }}
                    RETURN output LIMIT {self.graph_max_retrieved}""",
                {"query":self._generate_full_text_query(entity)}
            )

            results.extend([el['output'] for el in r])
            # result += "\n".join([el['output'] for el in r])

        return results


    def _generate_full_text_query(self,input:str) -> str:
        full_text_query = ""
        words = [el for el in remove_lucene_chars(input).split() if el]
        for word in words[:-1]:
            full_text_query += f" {word}~2 AND"
        full_text_query += f" {words[-1]}~2"
        return full_text_query.strip()

    def _extract_entities(self,query:str) -> list[str]:

        # Not sure if providing existing nodes/entities is good
        system_prompt = f"""You are extracting entities from text. Make sure the entities are specific (e.g. "Marie Curie" instead of "She" if it is implied). Respond with a JSON list of strings. Do not output any formatting or commentary. Always follow these rules. """

        saved = self.llm.system_prompt
        self.llm.system_prompt = system_prompt


        r = self.llm.generate(f"Extract entities from this text and make sure you output just raw json without any formatting: {query}")

        entities = json.loads(r)
        self.llm.system_prompt = saved
        return entities

    def remove_conversation(self, conversation_id: int) -> None:
        return None


if __name__ == "__main__":

    from llm import BielikLLM,OpenRouterLLM
    import os
    from tokenizer import RecursiveTokenizer

    llm=OpenAILLM(
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    #llm= BielikLLM(
    #    api_url=os.getenv("PG_LLM_URL"),
    #    llm_username=os.getenv("PG_LLM_USERNAME"),
    #    llm_password=os.getenv("PG_LLM_PASSWORD"),
    #    temperature=0.0,
    #    system_prompt="You are a helpful assistant"
    #)

    #llm = OpenRouterLLM(api_key=os.getenv("OPENROUTER_API_KEY"))
    tokenizer = RecursiveTokenizer(chunk_size=100,chunk_overlap=25)
    embedder = LocalEmbedder(model_name="all-MiniLM-L6-v2",device="cuda")

    kgr = KGraphRAG(llm=llm,tokenizer=tokenizer,embedder=embedder,neo4j_uri="neo4j://localhost:7687")


    # should be a dcoument instead of a string
    doc ="""
    Marie Curie discovered polonium and radium. 
    She worked at the University of Paris. 
    She won two Nobel Prizes.
    """

    # kgr.process_document(0,doc)
    # print("========================")
    # print(kgr.process_query(0,"What did Marie curie discover?"))










