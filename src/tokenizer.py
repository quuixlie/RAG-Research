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



class RecursiveTokenizer(Tokenizer):
    def __init__(self,chunk_size:int,chunk_overlap:int):

        if chunk_size <= 0:
            raise Exception(f"chunk_size has to be greater than 0 (current is:{chunk_size})")

        if chunk_overlap <= 0:
            raise Exception(f"chunk_overlap has to be greater than 0 (current is:{chunk_overlap})")

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.splitter = langchain_text_splitters.RecursiveCharacterTextSplitter(chunk_size=chunk_size,chunk_overlap=chunk_overlap)

    @override
    def tokenize(self,text:str) -> list[str]:
        """
        Tries to split the chunks to be below or equal `self.chunk_size`
        by a parametrized list of characters ['\n\n','\n',' ',''] (paragraph,line,word,...)

        The fragments will overlap `self.chunk_overlap` at most
        """
        return self.splitter.split_text(text)

if __name__ == "__main__":

    sample_text = """
    This is the first paragraph and it is about some crazy doo it is super looooooooooooooooong.
    And it continueshere blablablabl

    This is other paragraph and it is shorter
    """

    chunk_size=40
    chunk_overlap=15

    fixed = FixedSizeTokenizer(chunk_size)
    print("========= FIXED ========")
    print(fixed.tokenize(sample_text))

    print("========= RECURSIVE ========")
    rec = RecursiveTokenizer(chunk_size,chunk_overlap)
    print(rec.tokenize(sample_text))


