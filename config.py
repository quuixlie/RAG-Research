import os
import logging


class ConfigTemplate:
    """
    Configuration base class for RAG (Retrieval-Augmented Generation).
    """

    def __init__(self, database_kwargs: dict, rag_architecture_name: str, embedder_name: str, embedder_kwargs: dict,
                 cross_encoder_name: str, cross_encoder_kwargs: dict,
                 tokenizer_name: str, tokenizer_kwargs: dict,
                 llm_name: str, llm_kwargs: dict, evaluation_llm_name: str, evaluation_kwargs: dict) -> None:
        self.database_kwargs = database_kwargs
        self.rag_architecture_name = rag_architecture_name
        self.embedder_name = embedder_name
        self.embedder_kwargs = embedder_kwargs
        self.cross_encoder_name = cross_encoder_name
        self.cross_encoder_kwargs = cross_encoder_kwargs
        self.tokenizer_name = tokenizer_name
        self.tokenizer_kwargs = tokenizer_kwargs
        self.llm_name = llm_name
        self.llm_kwargs = llm_kwargs
        self.evaluation_llm_name = evaluation_llm_name
        self.evaluation_kwargs = evaluation_kwargs



    def __repr__(self) -> str:
        return (f"Config (\n"
                f"  database_kwargs: {self.database_kwargs},\n"
                f"  rag_architecture_name: {self.rag_architecture_name},\n"
                f"  embedder_name: {self.embedder_name},\n"
                f"  embedder_kwargs: {self.embedder_kwargs},\n"
                f"  cross_encoder_name: {self.cross_encoder_name},\n"
                f"  cross_encoder_kwargs: {self.cross_encoder_kwargs},\n"
                f"  tokenizer_name: {self.tokenizer_name},\n"
                f"  tokenizer_kwargs: {self.tokenizer_kwargs}\n"
                f"  llm_name: {self.llm_name},\n"
                f"  llm_kwargs: {self.llm_kwargs}\n"
                f"  evaluation_llm_name: {self.evaluation_llm_name},\n"
                f"  evaluation_kwargs: {self.evaluation_kwargs}\n"
                f")")


# =========================== Configuration ===========================
class Config(ConfigTemplate):
    def __init__(self) -> None:
        super().__init__(
            database_kwargs = {
                "embedding_dimension": 1024, #384,
            },
            rag_architecture_name = "classic-rag",
            # embedder_name = "basic-embedder",
            # embedder_kwargs= {
            #     "sentence_transformer_name": "mixedbread-ai/mxbai-embed-large-v1",
            #     "device": "cuda",
            # },
            embedder_name= "openai-embedder",
            embedder_kwargs = {
                "api_key": os.getenv("OPENAI_API_KEY"),
                "model_name": "text-embedding-3-small",
                "dimension": 1024,
            },
            cross_encoder_name = "basic-cross-encoder",
            cross_encoder_kwargs = {
                "sentence_transformer_name": "cross-encoder/ms-marco-MiniLM-L-6-v2",
                "device": "cuda",
            },
            tokenizer_name = "fixed-size-tokenizer",
            tokenizer_kwargs = {
                "chunk_size": 2048,
            },
            llm_name = "chat-gpt",
            llm_kwargs = {
                "api_key": os.getenv("OPENAI_API_KEY"),
                "initial_prompt": "You are a helpful assistant.",
                "model_name": "gpt-3.5-turbo",
                "temperature": 0.0,
            },
            # llm_name = "open-router",
            # llm_kwargs = {
            #     "api_key": os.getenv("OPENROUTER_API_KEY"),
            #     "initial_prompt": "You are a helpful assistant. Answer the question based on the provided context.",
            #     "model_name": "deepseek/deepseek-chat-v3-0324:free",
            # }
            evaluation_llm_name="chat-gpt",
            evaluation_kwargs = {
                "llm_kwargs": {
                    "api_key": os.getenv("OPENAI_API_KEY"),
                    "initial_prompt": None,
                    "model_name": "gpt-3.5-turbo",
                    "temperature": 0,
                },
            }
        )

        # Set logging settings
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        )
