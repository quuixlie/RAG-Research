import dataclasses
import os
from src.cross_encoder import CrossEncoder,BasicCrossEncoder
from src.llm import LLM, BielikLLM,OpenAILLM, OpenRouterLLM
from src.embedder import Embedder, LocalEmbedder
from src.tokenizer import RecursiveTokenizer, Tokenizer,FixedSizeTokenizer
from src.database import DatabaseKwargs
from src.architectures.rag_architecture_factory import RAGArchitectureName
from src.architectures.rag_architecture_factory import RAGArchitectureName

@dataclasses.dataclass
class Config:
    embedder:Embedder
    llm:LLM
    evaluation_llm:LLM
    rag_architecture_name: RAGArchitectureName 
    cross_encoder:CrossEncoder 
    tokenizer:Tokenizer

    database_kwargs: DatabaseKwargs 

    neo4j_uri:str="neo4j://localhost:7687"
    neo4j_username:str="user"
    neo4j_password:str="your_password"


    """
    Configuration base class for RAG (Retrieval-Augmented Generation).
    """

default_config = Config(
    rag_architecture_name="kg-rag",
    tokenizer= RecursiveTokenizer(
        chunk_size=512,
        chunk_overlap=24
    ),
    embedder = LocalEmbedder(
        model_name='all-MiniLM-L6-v2',
        device='cuda'
    ),
    llm=OpenRouterLLM(
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    evaluation_llm=OpenRouterLLM(
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    #llm=OpenAILLM(
    #    api_key=os.getenv("OPENAI_API_KEY"),
    #),
    #evaluation_llm=OpenAILLM(
    #    api_key=os.getenv("OPENAI_API_KEY"),
    #),
    #llm=BielikLLM(
    #    api_url=os.getenv("PG_LLM_URL"),
    #    llm_username=os.getenv("PG_LLM_USERNAME"),
    #    llm_password=os.getenv("PG_LLM_PASSWORD"),
    #    temperature=0.0,
    #    system_prompt="You are a helpful assistant"
    #),
    #evaluation_llm=BielikLLM(
    #    api_url=os.getenv("PG_LLM_URL"),
    #    llm_username=os.getenv("PG_LLM_USERNAME"),
    #    llm_password=os.getenv("PG_LLM_PASSWORD"),
    #    temperature=0.0,
    #    system_prompt="You are a helpful assistant"
    #),
    database_kwargs= DatabaseKwargs(
    embedding_dimension=384
    ),
    cross_encoder= BasicCrossEncoder(
        cross_encoder_name="dada",
        sentence_transformer_name="cross-encoder/ms-marco-MiniLM-L-6-v2",
        device="cpu"
    )
)
