from abc import ABC, abstractmethod


class TokenizerTemplate(ABC):
    """
    Base class for tokenizers. This class defines the interface for tokenizers, which are used to convert text into tokens.
    A new tokenizer can be created by inheriting from this class and implementing the tokenize method.

    :param tokenizer_name: Name of the tokenizer
    """

    def __init__(self, tokenizer_name: str) -> None:
        self.tokenizer_name = tokenizer_name


    @abstractmethod
    def tokenize(self, text: str) -> list:
        """
        Tokenize the input text and return a list of tokens.

        :param text: Input text to be tokenized
        :return: List of tokens
        """

        pass