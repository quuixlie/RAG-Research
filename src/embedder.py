from abc import ABC, abstractmethod
from typing import Literal,get_args, override,cast, List
import openai
from sentence_transformers import SentenceTransformer
import langchain_core.embeddings as langchainembeddings
import numpy as np
import numpy.typing as npt

EmbeddingSize = Literal[8,16,32,64,128,256,384,768,1536]


class Embedder(ABC):
    """
    Embedder Base Class
    """

    @abstractmethod
    def embed(self,query:str) -> npt.NDArray[np.float64]:
        """
        Generates embeddings from a single string values

        returns: 
            Embeddings of that string
        """
        pass

    def embed_fragments(self,fragments:list[str]) -> list[npt.NDArray[np.float64]]:
        """
        Generates an embedding for each text fragments specified in `fragments`
        Args:
            fragments (list[str]): A list of text fragments to embed.

        returns: 
            list[list[float]]: A list of embedding for each input fragment in the same order as input.
        """
        return [self.embed(fragment) for fragment in fragments]


class LangchainEmbedderWrapper(langchainembeddings.Embeddings):

    def __init__(self,embedder:Embedder):
        self.embedder:Embedder = embedder

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return cast(List[List[float]],[x.tolist() for x in self.embedder.embed_fragments(texts)])

    def embed_query(self, text: str) -> List[float]:
        return cast(List[float],self.embedder.embed(text).tolist())

class OpenAIEmbedder(Embedder):
    ModelName = Literal['text-embedding-3-small']
    def __init__(self,
                 api_key:str,
                 model_name: 'OpenAIEmbedder.ModelName' = 'text-embedding-3-small',
                 embedding_size: EmbeddingSize | openai.NotGiven = openai.NOT_GIVEN
        ):

        if model_name not in get_args(self.ModelName):
            raise Exception(f"Invalid embedder model name: {model_name} (possible values are: {get_args(self.ModelName)})")

        if embedding_size not in get_args(EmbeddingSize):
            raise Exception(f"Invalid embedding size: {embedding_size} (possible values are: {get_args(EmbeddingSize)})")

        self.model_name:OpenAIEmbedder.ModelName = model_name
        self.embedding_size:EmbeddingSize | openai.NotGiven = embedding_size

        self.openai_client = openai.OpenAI(api_key=api_key)

    @override
    def embed(self,query:str) -> npt.NDArray[np.float64]:
        embedding = self.openai_client.embeddings.create(
            input=query,
            model=self.model_name,
            dimensions=self.embedding_size
        )
        return np.array(embedding.data[0].embedding)


class LocalEmbedder(Embedder):

    ModelName = Literal['all-MiniLM-L6-v2','all-mpnet-base-v2']

    def __init__(self,model_name: 'LocalEmbedder.ModelName' = 'all-mpnet-base-v2',
                 device:Literal['cpu','cuda'] = 'cuda'
                ):

        if model_name not in get_args(self.ModelName):
            raise Exception(f"Invalid embedder model name: {model_name} (possible values are: {get_args(self.ModelName)})")

        if device not in ['cpu','cuda']:
            raise Exception(f"Invalid embedder device: {device} (possible values are: ['cpu','cuda'])")


        self.model = SentenceTransformer(
            model_name_or_path=model_name,
            device=device
        )

    @override
    def embed(self,query:str) -> npt.NDArray[np.float64]:
        embeddings = self.model.encode(
            sentences=[query]
        )

        return embeddings[0]
    
    @override
    def embed_fragments(self,fragments:list[str]) -> list[npt.NDArray[np.float64]]:
        embeddings = self.model.encode(
            sentences=fragments
        )

        return [x for x in embeddings]



