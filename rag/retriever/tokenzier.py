from abc import ABC, abstractmethod


class _TokenizerTemplate(ABC):
    """
    Abstract base class for tokenizers.
    """

    def __init__(self):
        self.tokenizer_name = None


    @abstractmethod
    def tokenize(self, text: str) -> list:
        """
        Tokenize the input text and return a list of tokenized chunks.

        :param text: Input text to be tokenized
        :return: List of tokenized chunks
        """

        pass



class TokenizerFactory(_TokenizerTemplate):
    """
    Factory class for creating tokenizers.
    Set the tokenizer model by calling the set_tokenizer method with the desired tokenizer name.
    Then, you can use the tokenize method to tokenize text.

    :param tokenizer_name: Name of the tokenizer to be set
    """

    def __init__(self, tokenizer_name: str, **kwargs):
        super().__init__()
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
        if self.tokenizer_name != tokenizer_name:
            self.__change_tokenizer(tokenizer_name, **kwargs)


    def __change_tokenizer(self, tokenizer_name: str, **kwargs) -> None:
        """
        Change the tokenizer according to the specified name.

        :param tokenizer_name: Name of the tokenizer to be set
        :return: None
        """

        # Set the tokenizer name
        self.tokenizer_name = tokenizer_name

        match tokenizer_name:
            case "fixed-size":
                self.__tokenizer = _FixedSizeTokenizer(**kwargs)


    def tokenize(self, text: str) -> list:
        if self.__tokenizer is None:
            raise ValueError("Tokenizer not set. Please set a tokenizer before tokenizing.")

        return self.__tokenizer.tokenize(text)



class _FixedSizeTokenizer(_TokenizerTemplate):
    """
    Tokenizer that splits text into fixed-size chunks.

    :param chunk_size: Size of each chunk
    """

    def __init__(self, chunk_size: int):
        super().__init__()
        self.chunk_size = chunk_size


    def tokenize(self, text: str) -> list:
        """
        Tokenize the input text into fixed-size chunks.

        :param text: Input text to be tokenized
        :return: List of tokenized chunks
        """

        return [text[i:i + self.chunk_size] for i in range(0, len(text), self.chunk_size)]

