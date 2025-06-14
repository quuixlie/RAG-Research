from typing import Literal, override
import langchain_text_splitters
from pydantic import BaseModel
from math import ceil

from abc import ABC, abstractmethod

class Tokenizer(ABC):
    """
    Tokenizer base class
    """

    @abstractmethod
    def tokenize(self,text:str) -> list[str]:
        """
        Splits the text int chunks
        """
        pass

class FixedSizeTokenizer(Tokenizer):


    def __init__(self,chunk_size:int):
        if chunk_size < 0:
            raise Exception("Chunk size has to be greater than 0")

        self.chunk_size:int = chunk_size


    @override
    def tokenize(self,text:str) -> list[str]:
        """
        Splits the text into chunks of size `self.chunk_size`
        """
        return [text[i*self.chunk_size:min((i+1)*self.chunk_size,len(text))] for i in range(ceil(len(text)/self.chunk_size))]


class TextSplitterKwargs(BaseModel):
    chunk_size:int = 100
    chunk_overlap:int = 0

TextSplitterName = Literal["character-tiktoken","character-recursive","markdown"]

def text_splitter_factory(splitter_name: TextSplitterName ,args:TextSplitterKwargs = TextSplitterKwargs()) -> langchain_text_splitters.TextSplitter:

    match splitter_name:
        case "character-tiktoken":
            # This could be something else depending on the model, but cl100k_base is used for targeting gpt-4,gpt3-5
            encoding_name = "cl100k_base"
            return langchain_text_splitters.CharacterTextSplitter.from_tiktoken_encoder(encoding_name=encoding_name,chunk_size=args.chunk_size,chunk_overlap=args.chunk_overlap)
        case "character-recursive":
            return langchain_text_splitters.RecursiveCharacterTextSplitter(chunk_size=args.chunk_size,chunk_overlap=args.chunk_overlap)
        case "markdown":
            return langchain_text_splitters.MarkdownTextSplitter(chunk_size=args.chunk_size,chunk_overlap=args.chunk_overlap)


if __name__ == "__main__":

    fixed = FixedSizeTokenizer(10)
    print(fixed.tokenize("hello this is some very long string that i want to tokenize "))

    exit(0)


    markdown_test = """
    # Title
    
    This is a paragraph.
    
    ## Section
    
    More content here.
    
    Another paragraph.
    """

    def test_splitter(splitter,text):
        print("#####################################################")
        print("testing {:<20} splitter".format(repr(type(splitter))))
        print("#####################################################")
        chunks = splitter.split_text(text)

        for i,chunk in enumerate(chunks):
            print("chunk",i,"\n",chunk);



    markdown_splitter = text_splitter_factory("markdown")
    recursive_splitter = text_splitter_factory("character-recursive")
    tiktoken_splitter = text_splitter_factory("character-tiktoken")
    markdown_header_splitter = langchain_text_splitters.MarkdownHeaderTextSplitter(headers_to_split_on=[
        ("#","Title"),
        ("##","Section"),
        ("###","Detail"),
        ])

    test_splitter(markdown_splitter,markdown_test)
    test_splitter(markdown_header_splitter,markdown_test)
    test_splitter(recursive_splitter,markdown_test)
    test_splitter(tiktoken_splitter,markdown_test)






     








