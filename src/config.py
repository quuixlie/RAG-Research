import os
from pydantic import BaseModel

from src.cross_encoders.cross_encoder_factory import CrossEncoderKwargs, CrossEncoderName
from src.embedders.embedders import EmbedderName, EmbedderKwargs
from src.llms.llm_factory import LLMKwargs, LLMType
from src.rag_architectures.rag_architecture_factory import RAGArchitectureName
from src.text_splitters.text_splitter import TextSplitterName,TextSplitterKwargs
from src.rag_architectures.rag_architecture_factory import RAGArchitectureName
from src.databases.vector_database import DatabaseKwargs


class Config(BaseModel):
    database_kwargs: DatabaseKwargs = DatabaseKwargs()
    rag_architecture_name: RAGArchitectureName = "classic-rag"

    embedder_name: EmbedderName = "sentence-transformers/all-mpnet-base-v2"
    embedder_kwargs: EmbedderKwargs = EmbedderKwargs()

    cross_encoder_name: CrossEncoderName = "cross-encoder/ms-marco-MiniLM-L-6-v2"
    cross_encoder_kwargs: CrossEncoderKwargs = CrossEncoderKwargs()

    text_splitter_name: TextSplitterName = "character-tiktoken"
    text_splitter_kwargs: TextSplitterKwargs = TextSplitterKwargs()

    llm_type: LLMType = "open-router"
    llm_kwargs: LLMKwargs = LLMKwargs()

    evaluation_llm_name: LLMType = "open-router"
    evaluation_kwargs: LLMKwargs = LLMKwargs()

    """
    Configuration base class for RAG (Retrieval-Augmented Generation).
    """

default_config = Config(

    llm_kwargs=LLMKwargs(
        api_key=os.getenv("OPENROUTER_API_KEY")
    )

)
