# ============================ Models import ===========================
from rag.tokenizers.fixed_size_tokenizer import FixedSizeTokenizer
# ======================================================================

from rag.tokenizers.__tokenizer_template import TokenizerTemplate
import logging


class TokenizerFactory(TokenizerTemplate):
    """
    Factory class for creating tokenizers. This class allows you to set the tokenizer model by calling the set_tokenizer method
    with the desired tokenizer name. Then, you can use the tokenize method to tokenize text. You have to pass an existing
    tokenizer model and its parameters to the constructor.

    :param tokenizer_name: Name of the tokenizer to be set
    :param kwargs: Additional parameters for the tokenizer model
    """

    def __init__(self, tokenizer_name: str, **kwargs):
        super().__init__(tokenizer_name)
        self.__tokenizer = None
        self.set_tokenizer(tokenizer_name, **kwargs)


    def set_tokenizer(self, tokenizer_name: str, **kwargs) -> None:
        """
        Set the tokenizer name and change the tokenizer model.
        (If the new tokenizer name is different from the current one, change the tokenizer model)

        :param tokenizer_name: Name of the tokenizer to be set
        :return: None
        """

        # If the new tokenizer name is different from the current one, change the tokenizer (model)
        if self.tokenizer_name != tokenizer_name or self.__tokenizer is None:
            self.__change_tokenizer(tokenizer_name, **kwargs)


    def __change_tokenizer(self, tokenizer_name: str, **kwargs) -> None:
        """
        Change the tokenizer according to the specified name.

        :param tokenizer_name: Name of the tokenizer to be set
        :return: None
        """

        # Set the tokenizer name
        self.tokenizer_name = tokenizer_name

        # ============================= Switch between models =============================
        match tokenizer_name:
            case "fixed-size-tokenizer":
                self.__tokenizer = FixedSizeTokenizer(tokenizer_name, **kwargs)
            case _:
                raise ValueError(f"Unsupported tokenizer name: {tokenizer_name}. Please use a valid tokenizer name.")
        # ============================= Switch between models =============================


    def tokenize(self, text: str) -> list:
        """
        Tokenize the input text and return a list of tokens.

        :param text: Input text to be tokenized
        :return: List of tokens
        """

        logging.info(f"Tokenizing text: {len(text)} characters.")

        if self.__tokenizer is None:
            raise ValueError("Tokenizer not set. Please set a tokenizer before tokenizing.")

        list_of_tokens = self.__tokenizer.tokenize(text)

        logging.info(f"Tokenized text: {len(list_of_tokens)} tokens.")

        return list_of_tokens