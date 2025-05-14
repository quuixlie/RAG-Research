from rag.rag_architectures.__rag_architecture_template import RAGArchitectureTemplate
from rag.llms.llm_factory import LLMFactory
from rag.embedders.embedder_factory import EmbedderFactory
from rag.tokenizers.tokenizer_factory import TokenizerFactory
from database.vector_database import VectorDatabase
from config import ConfigTemplate
from pymupdf import Document


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
        pass


    def process_query(self, conversation_id: int, query: str) -> dict:
        """
        Process the query to extract relevant information. Returns the answer to the query based on the processed document.
        Conversation ID is used to identify the conversation and retrieve the relevant informations from the vector database collection.

        :param conversation_id: ID of the conversation
        :param query: Query to be processed
        :return: Response to the query
        """
        pass


    def remove_conversation(self, conversation_id: int) -> None:
        """
        Remove the conversation from the vector database.

        :param conversation_id: ID of the conversation
        :return: None
        """
        if self.vector_database.has_collection(conversation_id):
            self.vector_database.remove_collection(conversation_id) 
