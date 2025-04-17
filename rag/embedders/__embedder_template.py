from abc import ABC, abstractmethod
from numpy import ndarray


class EmbedderTemplate(ABC):
    """
    Base class for embedding models. This class defines the interface for embedding models, which are used to convert
    text into embeddings. A new embedding model can be created by inheriting from this class and implementing the encode method.

    :param embedder_name: Name of the embedding model
    """

    def __init__(self, embedder_name: str) -> None:
        self.embedder_name = embedder_name


    @abstractmethod
    def encode(self, fragments: list, show_progress_bar: bool = False) -> ndarray:
        """
        Encode a list of text fragments into embeddings.
        :param fragments: List of text fragments to encode
        :param show_progress_bar: Whether to show a progress bar
        :return: 2D numpy array of embeddings or 1D numpy array of embedding (if only one fragment is passed)
        """

        pass