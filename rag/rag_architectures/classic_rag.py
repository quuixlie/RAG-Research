from rag.rag_architectures.__rag_architecture_template import RAGArchitectureTemplate
from config import ConfigTemplate
from database.vector_database import VectorDatabase
from rag.utils.document_parser import parse_to_markdown
from rag.utils.prompt_builder import create_prompt
from rag.llms.llm_factory import LLMFactory
from rag.embedders.embedder_factory import EmbedderFactory
from rag.tokenizers.tokenizer_factory import TokenizerFactory
from pymupdf import Document


class ClassicRAG(RAGArchitectureTemplate):
    """
    Classic RAG architecture for generating answers based on a given question and context.
    This class is a classic implementation of the RAG architecture, which combines a retriever and a generator.
    It uses a retriever to find relevant documents and a generator to generate answers based on the retrieved documents.

    :param rag_architecture_name: Name of the RAG architecture
    :param config: Configuration object containing RAG settings
    """

    def __init__(self, rag_architecture_name: str, config: ConfigTemplate) -> None:
        super().__init__(rag_architecture_name)
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
        # Prepare the vector database for the conversation
        self.__prepare_vector_database(conversation_id)

        # Parse the document to markdown
        parsed_document_to_markdown = parse_to_markdown(document)

        # Embedding
        embeddings_with_text_pairs = self.__prepare_document_embeddings_with_corresponding_text(parsed_document_to_markdown)
        self.__store_embeddings_with_text_pairs(conversation_id, embeddings_with_text_pairs)


    def process_query(self, conversation_id: int, query: str) -> dict:
        """
        Process the query to extract relevant information. Returns the answer to the query based on the processed document.
        Conversation ID is used to identify the conversation and retrieve the relevant informations from the vector database collection.

        :param conversation_id: ID of the conversation
        :param query: Query to be processed
        :return: Answer to the query
        """

        # Get relevant documents to the query
        relevant_documents = self.__get_relevant_documents_by_query(conversation_id, query)

        # Build prompt
        prompt = create_prompt(query, relevant_documents)

        # Generate answer
        answer = self.llm.generate(prompt)

        # Create a response dictionary
        response = {
            "query": query,
            "answer": answer,
            "contexts": relevant_documents
        }

        return response


    def __prepare_vector_database(self, conversation_id: int) -> None:
        """
        Prepare the vector database for a conversation by creating a collection if it doesn't exist.

        :param conversation_id: ID of the conversation
        :return: None
        """

        # Create a collection for the conversation if it doesn't exist
        if not self.vector_database.has_collection(conversation_id):
            dim = self.config.database_kwargs["embedding_dimension"]
            self.vector_database.create_collection(conversation_id, dimension=dim)


    def remove_conversation(self, conversation_id: int) -> None:
        """
        Remove the vector database collection for a conversation if it exists.

        :param conversation_id: ID of the conversation
        :return: None
        """

        if self.vector_database.has_collection(conversation_id):
            self.vector_database.remove_collection(conversation_id)


    def __prepare_document_embeddings_with_corresponding_text(self, document: str) -> list:
        """
        Prepare document embeddings by splitting the document into fragments and vectorizing them.

        :param document: Document to be embedded
        :return: List of document fragments
        """

        # Split the document into fragments
        fragments = self.tokenizer.tokenize(document)

        # Vectorize the fragments
        embeddings = self.embedder.encode(fragments, show_progress_bar=True)

        # Create a list of dictionaries with text and embedding
        embeddings_with_text_pairs = [
            {
                "text": fragment,
                "embedding": embedding.tolist()
            } for fragment, embedding in zip(fragments, embeddings)
        ]

        return embeddings_with_text_pairs


    def __store_embeddings_with_text_pairs(self, conversation_id: int, data: list) -> None:
        """
        Store the embeddings with their corresponding text in the vector database.

        :param conversation_id: ID of the conversation
        :param data: List of tuples containing embeddings and their corresponding text
        :return: None
        """

        self.vector_database.insert_data(conversation_id, data)


    def __get_relevant_documents_by_query(self, conversation_id: int, query: str) -> list:
        """
        Get relevant documents by processing the query and searching the vector database.

        :param conversation_id: ID of the conversation
        :param query: Query to be processed
        :return: List of relevant documents
        """

        # Embedding
        query_embedding = self.embedder.encode([query], show_progress_bar=True)

        # Search the vector database
        results = self.vector_database.search(conversation_id, query_embedding.tolist())

        # Create a list of relevant documents (text only)
        result = []
        for i in results[0]:
            result.append(i['entity']['text'])

        return result