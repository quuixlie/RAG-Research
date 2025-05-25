from abc import ABC, abstractmethod
from pymupdf import Document


class RAGArchitectureTemplate(ABC):
    """
    Base class for RAG architectures. This class defines the interface for RAG architectures, which are used to
    generate answers based on a given question and context. A new RAG architecture can be created by inheriting from this
    class and implementing the process_document method and the process_query method.

    :param rag_architecture_name: Name of the RAG architecture
    """

    def __init__(self, rag_architecture_name: str) -> None:
        self.rag_architecture_name = rag_architecture_name


    @abstractmethod
    def process_document(self, conversation_id: int, document: Document) -> None:
        """
        Process the document to extract relevant information and store it in the vector database.
        Conversation ID is used to identify the conversation and store the document in the correct vector database collection.

        :param conversation_id: ID of the conversation
        :param document: Document to be processed
        :return: None
        """
        pass


    @abstractmethod
    def process_query(self, conversation_id: int, query: str) -> dict:
        """
        Process the query to extract relevant information. Returns the answer to the query based on the processed document.
        Conversation ID is used to identify the conversation and retrieve the relevant informations from the vector database collection.

        :param conversation_id: ID of the conversation
        :param query: Query to be processed
        :return: Response to the query
        """
        pass


    @abstractmethod
    def remove_conversation(self, conversation_id: int) -> None:
        """
        Remove the conversation from the vector database.

        :param conversation_id: ID of the conversation
        :return: None
        """
        pass
