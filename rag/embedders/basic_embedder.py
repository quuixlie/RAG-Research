from sentence_transformers import SentenceTransformer
from rag.embedders.__embedder_template import EmbedderTemplate
from numpy import ndarray


class BasicEmbedder(EmbedderTemplate):
    """
    Basic embedder which uses SentenceTransformer to encode text fragments into embeddings.

    :param embedder_name: Name of the embedder
    """

    def __init__(self, embedder_name: str) -> None:
        super().__init__(embedder_name)
        self.__embedder = SentenceTransformer(embedder_name)


    def encode(self, fragments: list, show_progress_bar: bool = False) -> ndarray:
        """
        Encode a list of text fragments into embeddings.

        :param fragments: List of text fragments to encode
        :param show_progress_bar: Whether to show a progress bar
        :return: 2D numpy array of embeddings or 1D numpy array of embedding (if only one fragment is passed)
        """

        return self.__embedder.encode(fragments, show_progress_bar=show_progress_bar)