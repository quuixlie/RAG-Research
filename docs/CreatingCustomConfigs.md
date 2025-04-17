# Creating a custom config
This document provides a guide on how to create a new config for the RAG (Retrieval-Augmented Generation) framework. The process involves creating a new class in `config.py` that inherits from the base class `ConfigTemplate`.

### About the config
The config is a class that contains all the parameters needed to create a RAG architecture.
It is passed to the `RagArchitectureFactory` class, which is responsible for creating the RAG architecture based on the specified parameters.
The config class is designed to be flexible and extensible, allowing you to easily add new parameters or modify existing ones as needed.

- Every parameter with `kwargs` is corresponding to the parameters (in constructor, for example `chunk_size`) of the model (for example `FixedSizeTokenizer`) you want to use.
- Every parameter with `name` is corresponding to the name of the model (for example `ClassicRAG`) you want to use.
- (Optional) You can set logging settings in the config class. In the program, everything is logged on INFO level.
---

## To create a new config, follow these steps:
### 1. Specify how you want to name your config, for example, `ConfigName`.
### 2. Create a new class in `config.py` with the name `ConfigName`:
```python
...
# =========================== Configuration ===========================
class ConfigName(ConfigTemplate):
    def __init__(self) -> None:
        super().__init__(
            database_kwargs = {
            },
            rag_architecture_name = "",
            embedder_name = "",
            embedder_kwargs= {
            },
            tokenizer_name = "",
            tokenizer_kwargs = {
            },
            llm_name = "",
            llm_kwargs = {
            }
            # More parameters can be specified here if they are implemented in the ConfigTemplate class
        )

        # Set logging settings (optional, everything is logged on INFO level)
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        )
```
## Usage
```python
from config import ConfigName
from rag.rag_architectures.rag_architecture_factory import RagArchitectureFactory

config = ConfigName()
rag_architecture = RagArchitectureFactory(config.rag_architecture_name, config=config)

# Process query and document here
```