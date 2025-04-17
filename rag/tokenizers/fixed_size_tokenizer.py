from rag.tokenizers.__tokenizer_template import TokenizerTemplate


class FixedSizeTokenizer(TokenizerTemplate):
    """
    Fixed size tokenizer which tokenizes text into fixed-size tokens.
    This tokenizer is used for creating fixed-size embeddings from text.
    It is a subclass of TokenizerTemplate and implements the tokenize method.
    The tokenize method takes a string as input and returns a list of tokens.

    :param tokenizer_name: Name of the tokenizer
    :param chunk_size: Maximum length of the tokens
    """

    def __init__(self, tokenizer_name: str, chunk_size: int) -> None:
        super().__init__(tokenizer_name)
        self.chunk_size = chunk_size


    def tokenize(self, text: str) -> list:
        """
        Tokenize the input text into fixed-size tokens.

        :param text: Input text to be tokenized
        :return: List of fixed-size tokens
        """

        # Create fixed-size tokens
        return [text[i:i + self.chunk_size] for i in range(0, len(text), self.chunk_size)]