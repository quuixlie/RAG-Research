# Creating a new RAG architecture
This document describes how to create a new RAG (Retrieval-Augmented Generation) architecture in the RAG framework. The process involves creating a new class that inherits from the base class `RAGArchitectureTemplate` and implementing the required methods. Below are the steps to create a new RAG architecture.

---

## To create a new RAG architecture, follow these steps:
### 1. Specify how you want to name your architecture, for example, `RAGArchitectureName`.
### 2. Create a new file in the 'rag/rag_architectures' directory with the name `rag_architecture_name.py`.
### 3. Implement the RAG architecture class in the new file (it should implement the `process_document` and `process_query` methods). For example:
```python
from rag.rag_architectures.__rag_architecture_template import RAGArchitectureTemplate
from pymupdf import Document


class RAGArchitectureName(RAGArchitectureTemplate):
    """
    This is a custom RAG architecture class that inherits from RAGArchitectureTemplate.
    It implements the process_document and process_query methods to provide custom processing logic.
    
    :param architecture_name: Name of the architecture
    :param parameter1: Description of parameter1
    ...
    """
    def __init__(self, architecture_name: str, parameter1: str, ...) -> None:
        super().__init__(architecture_name)
        
        # Add your custom initialization code here
        self.parameter1 = parameter1
        
    def process_document(self, conversation_id: int, document: Document) -> str:
                """
        Process the document to extract relevant information and store it in the vector database.
        Conversation ID is used to identify the conversation and store the document in the correct vector database collection.

        :param conversation_id: ID of the conversation
        :param document: Document to be processed
        :return: None
        """
        # Implement your custom document processing logic here
        pass

    def process_query(self, conversation_id: int, query: str) -> str:
        """
        Process the query to extract relevant information. Returns the answer to the query based on the processed document.
        Conversation ID is used to identify the conversation and retrieve the relevant informations from the vector database collection.

        :param conversation_id: ID of the conversation
        :param query: Query to be processed
        :return: Answer to the query
        """
        # Implement your custom query processing logic here
        pass
```
### 4. Go to the 'rag/rag_architectures/rag_architecture_factory.py' file and add your architecture to the `RAGArchitectureFactory` class by importing the new architecture class and modifying the `__change_rag_architecture` method:
```python
# ============================ Models import ===========================
from rag.rag_architectures.rag_architecture_name import RAGArchitectureName
# ======================================================================

from rag.rag_architectures.__rag_architecture_template import RAGArchitectureTemplate
from pymupdf import Document


class RAGArchitectureFactory(RAGArchitectureTemplate):
    """
    Factory class for creating RAG architectures. This class allows you to set the RAG architecture by calling the set_rag_architecture method
    with the desired architecture name. Then, you can use the process_document and process_query methods to process documents and queries.
    You have to pass an existing RAG architecture and its parameters to the constructor.

    :param rag_architecture_name: Name of the RAG architecture to be set
    :param kwargs: Additional parameters for the RAG architecture
    """

    def __init__(self, rag_architecture_name: str, **kwargs) -> None:
        pass 


    def get_rag_architecture(self):
        pass


    def set_rag_architecture(self, rag_architecture_name: str, **kwargs) -> None:
        pass
        

    def __change_rag_architecture(self, rag_architecture_name: str, **kwargs) -> None:
        """
        Change the RAG architecture according to the specified name.

        :param rag_architecture_name: Name of the RAG architecture to be set
        :return: None
        """

        # Set the RAG architecture name
        self.rag_architecture_name = rag_architecture_name

        # ============================= Switch between architectures =============================
        match rag_architecture_name:
            case "rag_architecture_name":
                self.rag_architecture = RAGArchitectureName(rag_architecture_name, **kwargs)
            case _:
                raise ValueError(f"Unsupported RAG architecture name: {rag_architecture_name}. Please use a valid RAG architecture name.")
        # ======================================================================================


    def process_document(self, conversation_id: int, document: Document) -> None:
        pass

    def process_query(self, conversation_id: int, query: str) -> str:
        pass
```
## Usage of the new RAG architecture
```python
from rag.rag_architectures.rag_architecture_factory import RAGArchitectureFactory
from pymupdf import Document

document = Document("path/to/document.pdf")

# Create a new RAG architecture
rag_architecture = RAGArchitectureFactory("rag_architecture_name", parameter1="value1")

# Process the document
rag_architecture.process_document(conversation_id=1, document=document)
response = rag_architecture.process_query(conversation_id=1, query="What is the capital of France?")
print(response)
```