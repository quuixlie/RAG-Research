# ============================ Architectures import ===========================
from rag.rag_architectures.classic_rag import ClassicRAG
# =============================================================================

from rag.rag_architectures.__rag_architecture_template import RAGArchitectureTemplate


class RAGArchitectureFactory(RAGArchitectureTemplate):
    """
    Factory class for creating RAG architectures. This class allows you to set the RAG architecture by calling the set_rag_architecture method
    with the desired architecture name. Then, you can use the process_document and process_query methods to process documents and queries.
    You have to pass an existing RAG architecture and its parameters to the constructor.

    :param rag_architecture_name: Name of the RAG architecture to be set
    :param kwargs: Additional parameters for the RAG architecture
    """

    def __init__(self, rag_architecture_name: str, **kwargs) -> None:
        super().__init__(rag_architecture_name)
        self.__rag_architecture = None
        self.set_rag_architecture(rag_architecture_name, **kwargs)


    def set_rag_architecture(self, rag_architecture_name: str, **kwargs) -> None:
        """
        Set the RAG architecture name and change the RAG architecture.
        (If the new RAG architecture name is different from the current one, change the RAG architecture)

        :param rag_architecture_name: Name of the RAG architecture to be set
        :return: None
        """

        # If the new RAG architecture name is different from the current one, change the RAG architecture (model)
        if self.rag_architecture_name != rag_architecture_name:
            self.__change_rag_architecture(rag_architecture_name, **kwargs)


    def __change_rag_architecture(self, rag_architecture_name: str, **kwargs) -> None:
        """
        Change the RAG architecture according to the specified name.

        :param rag_architecture_name: Name of the RAG architecture to be set
        :return: None
        """

        # Set the RAG architecture name
        self.rag_architecture_name = rag_architecture_name

        # ============================= Switch between architectures =============================
        match rag_architecture_name:
            case "classic-rag":
                self.__rag_architecture = ClassicRAG(rag_architecture_name, **kwargs)
            case _:
                raise ValueError(f"Unsupported RAG architecture name: {rag_architecture_name}. Please use a valid RAG architecture name.")
        # ======================================================================================


    def process_document(self, conversation_id: int, document, config) -> None:
        """
        Process the document to extract relevant information and store it in the vector database.
        Conversation ID is used to identify the conversation and store the document in the correct vector database collection.

        :param conversation_id: ID of the conversation
        :param document: Document to be processed
        :param config: Configuration object containing RAG settings
        :return: None
        """
        return self.__rag_architecture.process_document(conversation_id, document, config)


    def process_query(self, conversation_id: int, query: str, config) -> str:
        """
        Process the query to extract relevant information. Returns the answer to the query based on the processed document.
        Conversation ID is used to identify the conversation and retrieve the relevant informations from the vector database collection.

        :param conversation_id: ID of the conversation
        :param query: Query to be processed
        :param config: Configuration object containing RAG settings
        :return: Answer to the query
        """
        return self.__rag_architecture.process_query(conversation_id, query, config)
    