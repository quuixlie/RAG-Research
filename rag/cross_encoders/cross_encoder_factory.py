# ============================ Models import ===========================
from rag.cross_encoders.basic_cross_encoder import BasicCrossEncoder
# ======================================================================


from rag.cross_encoders.__cross_encoder_template import CrossEncoderTemplate
import logging


class CrossEncoderFactory(CrossEncoderTemplate):
    """
    Factory class for creating cross-encoder models. This class allows you to set the cross-encoder model by calling the
    set_cross_encoder method with the desired cross-encoder name. Then, you can use the compare method to compute
    similarity scores between pairs of text fragments. You have to pass an existing
    cross-encoder model and its parameters to the constructor.

    :param cross_encoder_name: Name of the cross-encoder model to be set
    :param kwargs: Additional parameters for the cross-encoder
    """
    def __init__(self, cross_encoder_name: str, **kwargs) -> None:
        super().__init__(cross_encoder_name)
        self.__cross_encoder = None
        self.set_cross_encoder(cross_encoder_name, **kwargs)


    def set_cross_encoder(self, cross_encoder_name: str, **kwargs) -> None:
        """
        Set the cross-encoder model name and change the cross-encoder model.
        (If the new cross-encoder name is different from the current one, change the cross-encoder (model))

        :param cross_encoder_name: Name of the cross-encoder model to be set
        :return: None
        """

        # If the new cross-encoder name is different from the current one, change the cross-encoder (model)
        if self.cross_encoder_name != cross_encoder_name or self.__cross_encoder is None:
            self.__change_cross_encoder(cross_encoder_name, **kwargs)


    def __change_cross_encoder(self, cross_encoder_name: str, **kwargs) -> None:
        """
        Change the cross-encoder model according to the specified name.

        :param cross_encoder_name: Name of the cross-encoder model to be set
        :return: None
        """

        # Set the cross-encoder name
        self.cross_encoder_name = cross_encoder_name

        # ============================= Switch between models =============================
        match cross_encoder_name:
            case "basic-cross-encoder":
                self.__cross_encoder = BasicCrossEncoder(cross_encoder_name, **kwargs)
            case _:
                raise ValueError(f"Unsupported cross-encoder name: {cross_encoder_name}. Please use a valid cross-encoder name.")
        # =================================================================================


    def compare(self, pairs: list[tuple[str, str]]) -> list[float]:
        """
        Compare pairs of text fragments and return a list of similarity scores.

        :param pairs: List of pairs of text fragments to compare
        :return: List of similarity scores
        """
        logging.info(f"Comparing {len(pairs)} pairs of text fragments using {self.cross_encoder_name} cross-encoder.")

        # Check if the cross-encoder is set
        if self.__cross_encoder is None:
            raise ValueError("Cross-encoder model is not set. Please set the cross-encoder model before comparing.")
        
        # Compare the pairs using the cross-encoder
        scores = self.__cross_encoder.compare(pairs)

        logging.info(f"Cross-encoder: {self.cross_encoder_name} - Comparison completed.")
        return scores