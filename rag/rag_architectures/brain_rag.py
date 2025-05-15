from rag.rag_architectures.__rag_architecture_template import RAGArchitectureTemplate
from rag.llms.llm_factory import LLMFactory
from rag.embedders.embedder_factory import EmbedderFactory
from rag.tokenizers.tokenizer_factory import TokenizerFactory
from database.vector_database import VectorDatabase
from config import ConfigTemplate
from pymupdf import Document
from rag.utils.prompt_builder import create_prompt
from rag.utils.document_parser import parse_to_markdown


class BrainRAG(RAGArchitectureTemplate):
    """

    """

    def __init__(self, rag_architecture_name: str, config: ConfigTemplate) -> None:
        self.rag_architecture_name = rag_architecture_name
        self.config = config
        self.embedder = EmbedderFactory(self.config.embedder_name, **self.config.embedder_kwargs)
        self.tokenizer = TokenizerFactory(self.config.tokenizer_name, **self.config.tokenizer_kwargs)
        self.llm = LLMFactory(self.config.llm_name, **self.config.llm_kwargs)
        self.vector_database = VectorDatabase()



    def process_document(self, conversation_id: int, document: Document) -> None:
        """
        Process the document to extract relevant information and store it in the vector database.
        Conversation ID is used to identify the conversation and store the document in the correct vector database collection.

        :param conversation_id: ID of the conversation
        :param document: Document to be processed
        :return: None
        """
        # Create a new collection for the conversation
        self.vector_database.create_collection(conversation_id, dimension=self.config.database_kwargs["embedding_dimension"])

        # Parse the document to markdown
        parsed_document_to_markdown = parse_to_markdown(document)
        fragments = self.tokenizer.tokenize(parsed_document_to_markdown)
        data_to_insert = []
        for fragment in fragments:
            # Get the questions to fragment
            questions = self.get_questions_to_fragment(fragment)

            # Embed the fragment
            embedding = self.embedder.encode(questions)
        
            data_to_insert.append({
                "text": fragment,
                "embedding": embedding.tolist(),
            })

        # Store the embeddings with text pairs in the vector database
        self.vector_database.insert_data(conversation_id, data_to_insert)




    def process_query(self, conversation_id: int, query: str) -> dict:
        """
        Process the query to extract relevant information. Returns the answer to the query based on the processed document.
        Conversation ID is used to identify the conversation and retrieve the relevant informations from the vector database collection.

        :param conversation_id: ID of the conversation
        :param query: Query to be processed
        :return: Response to the query
        """
        query_embedding = self.embedder.encode([query])

        results = self.vector_database.search(conversation_id, query_embedding.tolist())

        # Create a list of relevant documents (text only)
        result = []
        for i in results[0]:
            result.append(i['entity']['text'])  

        # Build prompt
        prompt = create_prompt(query, result)   

        # Generate answer
        answer = self.llm.generate(prompt)

        response = {
            "query": query,
            "answer": answer,
            "contexts": result
        }

        return response  


    def remove_conversation(self, conversation_id: int) -> None:
        """
        Remove the conversation from the vector database.

        :param conversation_id: ID of the conversation
        :return: None
        """
        if self.vector_database.has_collection(conversation_id):
            self.vector_database.remove_collection(conversation_id) 


    def get_questions_to_fragment(self, fragment: str) -> str:
        """
        Get the questions to fragment.

        :param fragment: Fragment to be processed
        :return: Questions to fragment
        """
        
        prompt = f"""
            Based on the following text, generate a list of questions that a reader might ask to better understand, analyze, or remember the content. Include factual questions (who, what, when, where, why, how), comprehension questions, and interpretive questions. Do not answer the questions — only list them.

            Text:
            {fragment}

            Expected output format:

                Question 1

                Question 2

                Question 3
                
                ..."""
        
        # Generate the questions using the LLM
        questions = self.llm.generate(prompt)

        return questions
