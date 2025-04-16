from abc import ABC, abstractmethod
from numpy import ndarray
from sentence_transformers import SentenceTransformer


class _EmbedderTemplate(ABC):
    """
    Base class for embedding models. This class defines the interface for embedding models, which are used to convert
    text into embeddings.
    """

    def __init__(self):
        self.embedder_name = None


    @abstractmethod
    def encode(self, fragments: list, show_progress_bar: bool = False) -> list:
        """
        Encode a list of text fragments into embeddings.
        :param fragments: List of text fragments to encode
        :param show_progress_bar: Whether to show a progress bar
        :return: List of embeddings
        """

        pass


class EmbedderFactory(_EmbedderTemplate):
    """
    Factory class for creating embedding models. This class allows you to set the embedding model by calling the
    set_embedder method with the desired embedder name. Then, you can use the encode method to convert list of texts into
    embeddings.

    :param embedder_name: Name of the embedding model to be set
    """

    def __init__(self, embedder_name: str, **kwargs):
        super().__init__()
        self.__embedder = None
        self.set_embedder(embedder_name, **kwargs)


    def set_embedder(self, embedder_name: str, **kwargs) -> None:
        """
        Set the embedding model name and change the embedding model.
        (If the new embedder name is different from the current one, change the embedding model)

        :param embedder_name: Name of the embedding model to be set
        :return: None
        """

        # If the new embedder name is different from the current one, change the embedder (model)
        if self.embedder_name != embedder_name:
            self.__change_embedder(embedder_name, **kwargs)


    def __change_embedder(self, embedder_name: str, **kwargs) -> None:
        """
        Change the embedding model according to the specified name.

        :param embedder_name: Name of the embedding model to be set
        :return: None
        """

        # Set the embedder name
        self.embedder_name = embedder_name

        match embedder_name:
            case "sentence-transformers/all-MiniLM-L12-v2":
                self.__embedder = SentenceTransformer(embedder_name, **kwargs)
            case _:
                raise ValueError(f"Unsupported embedder name: {embedder_name}. Please use a valid embedder name.")


    def encode(self, fragments: list, show_progress_bar: bool = False) -> ndarray:
        """
        Encode a list of text fragments into embeddings.

        :param fragments: List of text fragments to encode
        :param show_progress_bar: Whether to show a progress bar
        :return: 2D numpy array of embeddings or 1D numpy array of embedding (if only one fragment is passed)
        """

        if self.__embedder is None:
            raise ValueError("Embedder not set. Please set an embedder before encoding.")

        return self.__embedder.encode(fragments, show_progress_bar=show_progress_bar)
