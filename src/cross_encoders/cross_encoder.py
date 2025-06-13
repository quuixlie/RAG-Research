from abc import ABC, abstractmethod
from typing import override
import sentence_transformers as st


class CrossEncoder(ABC):
    """
    Base class for cross-encoder models. This class defines the interface for cross-encoder models, which are used to
    compute similarity scores between pairs of text fragments. A new cross-encoder model can be created by inheriting
    from this class and implementing the encode method.

    :param cross_encoder_name: Name of the cross-encoder model
    """

    def __init__(self, cross_encoder_name: str) -> None:
        self.cross_encoder_name = cross_encoder_name

    
    @abstractmethod
    def compare(self, pairs: list[tuple[str, str]]) -> list[float]:
        """
        Compare pairs of text fragments and return a list of similarity scores.

        :param pairs: List of pairs of text fragments to compare
        :return: List of similarity scores
        """
        pass


class BasicCrossEncoder(CrossEncoder):
    """
    Basic cross-encoder which uses SentenceTransformer to compute similarity scores between pairs of text fragments.
    """

    def __init__(self, cross_encoder_name: str, sentence_transformer_name: str, device: str) -> None:
        super().__init__(cross_encoder_name)
        self.__cross_encoder = st.CrossEncoder(sentence_transformer_name, device=device)


    @override
    def compare(self, pairs: list[tuple[str, str]], show_progress_bar: bool = False) -> list[float]:
        """
        Compute similarity scores between pairs of text fragments.

        :param pairs: List of pairs of text fragments to compare
        :param show_progress_bar: Whether to show a progress bar
        :return: List of similarity scores
        """

        scores = self.__cross_encoder.predict(pairs, show_progress_bar=show_progress_bar)

        # Scores to list
        scores = scores.tolist()

        return scores
