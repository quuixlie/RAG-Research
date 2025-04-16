import os


class ConfigTemplate:
    """
    Configuration base class for RAG (Retrieval-Augmented Generation).
    """

    def __init__(self, embedding_model: str, embedding_kwargs: dict, tokenizer_name: str, tokenizer_kwargs: dict,
                 llm_name: str, llm_kwargs: dict) -> None:
        self.embedding_model = embedding_model
        self.embedding_kwargs = embedding_kwargs
        self.tokenizer_name = tokenizer_name
        self.tokenizer_kwargs = tokenizer_kwargs
        self.llm_name = llm_name
        self.llm_kwargs = llm_kwargs


    def __repr__(self) -> str:
        return (f"Config (\n"
                f"  embedding_model: {self.embedding_model},\n"
                f"  embedding_kwargs: {self.embedding_kwargs},\n"
                f"  tokenizer_name: {self.tokenizer_name},\n"
                f"  tokenizer_kwargs: {self.tokenizer_kwargs}\n"
                f"  llm_name: {self.llm_name},\n"
                f"  llm_kwargs: {self.llm_kwargs}\n"
                f")")


# =========================== Configuration ===========================
class Config(ConfigTemplate):
    def __init__(self) -> None:
        super().__init__(
            embedding_model = "sentence-transformers/all-MiniLM-L12-v2",
            embedding_kwargs= {
                "device": "cuda",
                "dimension": 384,
            },
            tokenizer_name = "fixed-size",
            tokenizer_kwargs = {
                "chunk_size": 256
            },
            llm_name = "OpenAI",
            llm_kwargs = {
                "api_key": os.getenv("OPENAI_API_KEY"),
            }
        )
