from abc import ABC, abstractmethod


class CrossEncoderTemplate(ABC):
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