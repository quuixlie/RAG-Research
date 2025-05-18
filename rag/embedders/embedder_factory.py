# ============================ Models import ===========================
from rag.embedders.basic_embedder import BasicEmbedder
from rag.embedders.openai_embedder import OpenAIEmbedder
# ======================================================================


from rag.embedders.__embedder_template import EmbedderTemplate
from numpy import ndarray
import logging


class EmbedderFactory(EmbedderTemplate):
    """
    Factory class for creating embedding models. This class allows you to set the embedding model by calling the
    set_embedder method with the desired embedder name. Then, you can use the encode method to convert list of texts into
    embeddings. You have to pass an existing embedding model and its parameters to the constructor.

    :param embedder_name: Name of the embedding model to be set
    :param kwargs: Additional parameters for the embedding model
    """

    def __init__(self, embedder_name: str, **kwargs):
        super().__init__(embedder_name)
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
        if self.embedder_name != embedder_name or self.__embedder is None:
            self.__change_embedder(embedder_name, **kwargs)


    def __change_embedder(self, embedder_name: str, **kwargs) -> None:
        """
        Change the embedding model according to the specified name.

        :param embedder_name: Name of the embedding model to be set
        :return: None
        """

        # Set the embedder name
        self.embedder_name = embedder_name

        # ============================= Switch between models =============================
        match embedder_name:
            case "basic-embedder":
                self.__embedder = BasicEmbedder(embedder_name, **kwargs)
            case "openai-embedder":
                self.__embedder = OpenAIEmbedder(embedder_name, **kwargs)
            case _:
                raise ValueError(f"Unsupported embedder name: {embedder_name}. Please use a valid embedder name.")
        # =================================================================================


    def encode(self, fragments: list, show_progress_bar: bool = False) -> ndarray:
        """
        Encode a list of text fragments into embeddings.

        :param fragments: List of text fragments to encode
        :param show_progress_bar: Whether to show a progress bar
        :return: 2D numpy array of embeddings or 1D numpy array of embedding (if only one fragment is passed)
        """

        logging.info(f"Embedder: {self.embedder_name} - Encoding {len(fragments)} fragments.")

        if self.__embedder is None:
            raise ValueError("Embedder not set. Please set an embedder before encoding.")

        embeddings = self.__embedder.encode(fragments, show_progress_bar=show_progress_bar)

        logging.info(f"Embedder: {self.embedder_name} - Finished encoding {len(fragments)} fragments.")

        return embeddings
