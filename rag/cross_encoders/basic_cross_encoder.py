from sentence_transformers import CrossEncoder
from rag.cross_encoders.__cross_encoder_template import CrossEncoderTemplate
import os


class BasicCrossEncoder(CrossEncoderTemplate):
    """
    Basic cross-encoder which uses SentenceTransformer to compute similarity scores between pairs of text fragments.
    """

    def __init__(self, cross_encoder_name: str, sentence_transformer_name: str, device: str) -> None:
        super().__init__(cross_encoder_name)
        self.__cross_encoder = CrossEncoder(sentence_transformer_name, device=device)


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