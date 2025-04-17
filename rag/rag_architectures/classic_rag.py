from rag.rag_architectures.__rag_architecture_template import RAGArchitectureTemplate
from config import ConfigTemplate


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


    def process_document(self, conversation_id: int, document, config: ConfigTemplate) -> None:
        """
        Process the document to extract relevant information and store it in the vector database.
        Conversation ID is used to identify the conversation and store the document in the correct vector database collection.

        :param conversation_id: ID of the conversation
        :param document: Document to be processed
        :param config: Configuration object containing RAG settings
        :return: None
        """
        pass


    def process_query(self, conversation_id: int, query: str, config: ConfigTemplate) -> str:
        """
        Process the query to extract relevant information. Returns the answer to the query based on the processed document.
        Conversation ID is used to identify the conversation and retrieve the relevant informations from the vector database collection.

        :param conversation_id: ID of the conversation
        :param query: Query to be processed
        :param config: Configuration object containing RAG settings
        :return: Answer to the query
        """
        pass
