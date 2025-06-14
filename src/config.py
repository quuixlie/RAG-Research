import dataclasses
import os
from .cross_encoder import CrossEncoder,BasicCrossEncoder
from .llm import LLM, BielikLLM
from .embedder import Embedder, LocalEmbedder
from .tokenizer import Tokenizer,FixedSizeTokenizer
from .vector_database import DatabaseKwargs
from .architectures.rag_architecture_factory import RAGArchitectureName
from .architectures.rag_architecture_factory import RAGArchitectureName


@dataclasses.dataclass
class Config:

    embedder:Embedder
    llm:LLM
    evaluation_llm:LLM
    rag_architecture_name: RAGArchitectureName 
    cross_encoder:CrossEncoder 
    tokenizer:Tokenizer

    database_kwargs: DatabaseKwargs 
    database_kwargs: DatabaseKwargs 


    """
    Configuration base class for RAG (Retrieval-Augmented Generation).
    """

default_config = Config(
    tokenizer= FixedSizeTokenizer(
        chunk_size=15
    ),
    embedder = LocalEmbedder(
        model_name='all-MiniLM-L6-v2',
        device='cpu'
    ),
    llm=BielikLLM(
        api_url=os.getenv("PG_LLM_URL"),
        llm_username=os.getenv("PG_LLM_USERNAME"),
        llm_password=os.getenv("PG_LLM_PASSWORD"),
        temperature=0.0,
        initial_prompt="You are a helpful assistant"
    ),
    evaluation_llm=BielikLLM(
        api_url=os.getenv("PG_LLM_URL"),
        llm_username=os.getenv("PG_LLM_USERNAME"),
        llm_password=os.getenv("PG_LLM_PASSWORD"),
        temperature=0.0,
        initial_prompt="You are a helpful assistant"
    ),
    database_kwargs= DatabaseKwargs(
    embedding_dimension=384
    ),
    rag_architecture_name= "classic-rag",
    cross_encoder= BasicCrossEncoder(
        cross_encoder_name="dada",
        sentence_transformer_name="cross-encoder/ms-marco-MiniLM-L-6-v2",
        device="cpu"
    )

)
