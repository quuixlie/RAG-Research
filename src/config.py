import dataclasses
import os
from pydantic import BaseModel
from .cross_encoders.cross_encoder import CrossEncoder,BasicCrossEncoder
from .llms.llm import LLM, BielikLLM
from .embedders.embedder import Embedder, LocalEmbedder
from .rag_architectures.rag_architecture_factory import RAGArchitectureName
from .text_splitters.text_splitter import TextSplitterName,TextSplitterKwargs
from .rag_architectures.rag_architecture_factory import RAGArchitectureName
from .databases.vector_database import DatabaseKwargs


@dataclasses.dataclass
class Config:

    embedder:Embedder
    llm:LLM
    evaluation_llm:LLM
    database_kwargs: DatabaseKwargs 
    rag_architecture_name: RAGArchitectureName 
    cross_encoder:CrossEncoder 
    text_splitter_name: TextSplitterName
    text_splitter_kwargs: TextSplitterKwargs 


    """
    Configuration base class for RAG (Retrieval-Augmented Generation).
    """

default_config = Config(
    embedder = LocalEmbedder(
        model_name='all-MiniLM-L6-v2',
        device='cpu'
    ),
    llm=BielikLLM(
        api_url=os.getenv("PG_API_URL"),
        llm_username=os.getenv("PG_LLM_USERNAME"),
        llm_password=os.getenv("PG_LLM_PASSWORD"),
        temperature=0.0,
        initial_prompt="You are a helpful assistant"
    ),
    evaluation_llm=BielikLLM(
        api_url=os.getenv("PG_API_URL"),
        llm_username=os.getenv("PG_LLM_USERNAME"),
        llm_password=os.getenv("PG_LLM_PASSWORD"),
        temperature=0.0,
        initial_prompt="You are a helpful assistant"
    ),
    database_kwargs= DatabaseKwargs(
    embedding_dimension=384
    ),
    rag_architecture_name= "classic-rag",
    text_splitter_name= "character-tiktoken",
    text_splitter_kwargs= TextSplitterKwargs(),
    cross_encoder= BasicCrossEncoder(
        cross_encoder_name="dada",
        sentence_transformer_name="cross-encoder/ms-marco-MiniLM-L-6-v2",
        device="cpu"
    )

)
