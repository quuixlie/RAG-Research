import os
import logging


class ConfigTemplate:
    """
    Configuration base class for RAG (Retrieval-Augmented Generation).
    """

    def __init__(self,rag_architecture_name: str, rag_architecture_kwargs: dict,
                 llm_name: str, llm_kwargs: dict) -> None:
        self.rag_architecture_name = rag_architecture_name
        self.rag_architecture_kwargs = rag_architecture_kwargs
        self.llm_name = llm_name
        self.llm_kwargs = llm_kwargs


    def __repr__(self) -> str:
        return (f"Config (\n"
                f"  rag_architecture_name: {self.rag_architecture_name},\n"
                f"  rag_architecture_kwargs: {self.rag_architecture_kwargs},\n"
                f"  llm_name: {self.llm_name},\n"
                f"  llm_kwargs: {self.llm_kwargs}\n"
                f")")


# =========================== Configuration ===========================
class Config(ConfigTemplate):
    def __init__(self) -> None:
        super().__init__(
            rag_architecture_name = "classic-rag",
            rag_architecture_kwargs = {
                "embedder_name": "openai-embedder",
                "embedder_kwargs": {
                    "api_key": os.getenv("OPENAI_API_KEY"),
                    "model_name": "text-embedding-3-small",
                },
                "tokenizer_name": "openai-tokenizer",
                "tokenizer_kwargs": {
                    "api_key": os.getenv("OPENAI_API_KEY"),
                    "model_name": "gpt-3.5-turbo",
                },
            },
            llm_name = "chat-gpt",
            llm_kwargs = {
                "api_key": os.getenv("OPENAI_API_KEY"),
                "initial_prompt": "You are a helpful assistant.",
                "model_name": "gpt-3.5-turbo",
                "temperature": 0.0,
            },
        )

        # Set logging settings
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        )
