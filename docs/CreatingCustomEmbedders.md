# Creating a new embedder
This document provides a guide on how to create a new embedder for the RAG (Retrieval-Augmented Generation) framework. The process involves creating a new class that inherits from the base class `EmbedderTemplate` and implementing the required methods.

---

## To create a new embedder, follow these steps:
### 1. Specify how you want to name your embedder, for example, `EmbedderName`.
### 2. Create a new file in the 'rag/embedders' directory with the name `embedder_name.py`.
### 3. Implement the embedder class in the new file (it should implement the `encode` method). For example:
```python
from rag.embedders.__embedder_template import EmbedderTemplate
from numpy import ndarray


class EmbedderName(EmbedderTemplate):
    """
    This is a custom embedder class that inherits from EmbedderTemplate.
    It implements the encode method to provide custom embedding logic.
    
    :param embedder_name: Name of the embedder
    :param parameter1: Description of parameter1
    ...
    """
    def __init__(self, embedder_name: str, parameter1: str, ...) -> None:
        super().__init__(embedder_name)
        
        # Add your custom initialization code here
        self.parameter1 = parameter1
        
    def encode(self, fragments: list, show_progress_bar: bool = False) -> ndarray:
        """
        Encode a list of text fragments into embeddings.

        :param fragments: List of text fragments to encode
        :param show_progress_bar: Whether to show a progress bar
        :return: 2D numpy array of embeddings or 1D numpy array of embedding (if only one fragment is passed)
        """

        # Implement your custom embedding logic here
        pass
```
### 4. Go to the 'rag/embedders/embedder_factory.py' file and add your embedder to the `EmbedderFactory` class by importing the new embedder class and modifying the `__change_embedder` method:
```python
# ============================ Models import ===========================
from rag.embedders.embedder_name import EmbedderName
# ======================================================================


from rag.embedders.__embedder_template import EmbedderTemplate
from numpy import ndarray


class EmbedderFactory(EmbedderTemplate):
    """
    Factory class for creating embedding models. This class allows you to set the embedding model by calling the
    set_embedder method with the desired embedder name. Then, you can use the encode method to convert list of texts into
    embeddings. You have to pass an existing embedding model and its parameters to the constructor.

    :param embedder_name: Name of the embedding model to be set
    :param kwargs: Additional parameters for the embedding model
    """

    def __init__(self, embedder_name: str, **kwargs):
        pass 


    def set_embedder(self, embedder_name: str, **kwargs) -> None:
        pass 


    def __change_embedder(self, embedder_name: str, **kwargs) -> None:
        """
        Change the embedding model according to the specified name.

        :param embedder_name: Name of the embedding model to be set
        :return: None
        """

        # Set the embedder name
        self.embedder_name = embedder_name

        # ============================= Switch between models =============================
        match embedder_name:
            case "embedder-name":
                self.__embedder = EmbedderName(embedder_name, **kwargs)
            case _:
                raise ValueError(f"Unsupported embedder name: {embedder_name}. Please use a valid embedder name.")
        # =================================================================================


    def encode(self, fragments: list, show_progress_bar: bool = False) -> ndarray:
       pass 
```
## Usage of the new embedder
```python
# Initial embedder must be a valid one
from rag.embedders.embedder_factory import EmbedderFactory


# Creating a new embedder
embedder = EmbedderFactory("embedder-name", parameter1="value1")
embeddings = embedder.encode(fragments=["text to embed", "text to embed2"], show_progress_bar=True)

# If you want to change the embedder
embedder.set_embedder(embedder_name="embedder-name2", parameter1="value1")
embeddings = embedder.encode(fragments=["text to embed", "text to embed2"], show_progress_bar=True)
```