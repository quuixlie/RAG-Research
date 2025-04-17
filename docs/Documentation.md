# Installation
### Start milvus database (it will install docker image if not installed)
```bash
sudo ./milvus.sh start
```
or if you want to stop the database:
```bash
sudo ./milvus.sh stop
```



---
# Usage
TODO


---
# Creating a new tokenizer
### 1. Create a new class in 'rag/retriever/tokenizer.py' which inherits from the base class '_TokenizerTemplate'
```python
class _TokenizerName(_TokenizerTemplate):
    """
    This is a custom tokenizer class that inherits from _TokenizerTemplate.
    It implements the tokenize method to provide custom tokenization logic.
    
    :param parameter1: Description of parameter1
    ...
    """
    def __init__(self, parameter1: str ...):
        super().__init__()
        # Add your custom initialization code here
        pass

        
    def tokenize(self, text: str) -> list:
        """
        Tokenizes the input text into a list of chunks.
        
        :param text: The input text to tokenize
        :return: A list of tokenized chunks.
        """        
        
        # Implement your custom tokenization logic here
        pass
```
### 2. Add the new tokenizer to the 'TokenizerFactory' class in 'rag/retriever/tokenizer.py'. (Modify the private method '__change_tokenizer')
```python
class TokenizerFactory(_TokenizerTemplate):
    def __init__(self):
        pass

    
    def set_tokenizer(self):
        pass

    
    # **kwargs are the parameters that will be passed to the tokenizer (e.g. parameter1: str)
    def __change_tokenizer(self, tokenizer_name: str, **kwargs) -> None:
        """
        Change the tokenizer according to the specified name.

        :param tokenizer_name: Name of the tokenizer to be set
        :param kwargs: Additional parameters for the tokenizer
        :return: None
        """

        # Set the tokenizer name
        self.tokenizer_name = tokenizer_name
        
        match tokenizer_name:
            case "tokenizer-name":
                self.tokenizer = _TokenizerName(**kwargs)


    def tokenize(self):
        pass
```
### 3. Usage of the new tokenizer
```python
# Initial tokenizer must be a valid one
tokenizer = TokenizerFactory("tokenizer-name", parameter1="value1")
fragments = tokenizer.tokenize(text="text to tokenize")

# If you want to change the tokenizer
tokenizer.set_tokenizer(tokenizer_name="tokenizer-name2", parameter1="value1")
fragments = tokenizer.tokenize(text="text to tokenize")
```



---
# Creating a new embedder
### 1. Create a new class in 'rag/retriever/embedder.py' which inherits from the base class '_EmbedderTemplate'
```python
class _EmbedderName(_EmbedderTemplate):
    """
    This is a custom embedder class that inherits from _EmbedderTemplate.
    It implements the encode method to provide custom embedding logic.
    
    :param parameter1: Description of parameter1
    ...
    """
    def __init__(self, parameter1: str ...):
        super().__init__()
        # Add your custom initialization code here
        pass
    
        
    def encode(self, fragments: list, show_progress_bar: bool = False) -> ndarray:
        """
        Encodes the input fragments into a list of embeddings.

        :param fragments: The input fragments to encode
        :param show_progress_bar: Whether to show a progress bar during encoding
        :return: 2D numpy array of embeddings or 1D numpy array of embedding (if only one fragment is passed)
        """ 

        # Implement your custom embedding logic here
        pass
```
### 2. Add the new embedder to the 'EmbedderFactory' class in 'rag/retriever/embedder.py'. (Modify the private method '__change_embedder')
```python
class EmbedderFactory(_EmbedderTemplate):
    def __init__(self):
        pass

    
    def set_embedder(self):
        pass

    
    # **kwargs are the parameters that will be passed to the embedder (e.g. parameter1: str)
    def __change_embedder(self, embedder_name: str, **kwargs) -> None:
        """
        Change the embedder according to the specified name.

        :param embedder_name: Name of the embedder to be set
        :param kwargs: Additional parameters for the embedder
        :return: None
        """
        
        # Set the embedder name
        self.embedder_name = embedder_name
        
        match embedder_name:
            case "embedder-name":
                self.embedder = _EmbedderName(**kwargs)
                
                
    def encode(self):
        pass
```
### 3. Usage of the new embedder
```python
# Initial embedder must be a valid one
embedder = EmbedderFactory("embedder-name", parameter1="value1")
embeddings = embedder.encode(fragments=["text to embed", "text to embed2"], show_progress_bar=True)

# If you want to change the embedder
embedder.set_embedder(embedder_name="embedder-name2", parameter1="value1")
embeddings = embedder.encode(fragments=["text to embed", "text to embed2"], show_progress_bar=True)
```



---
# Creating a new llm model
### 1. Create a new class in 'rag/generator/llm_handler.py' which inherits from the base class '_LLMTemplate'
```python
class _LLMName(_LLMTemplate):
    """
    This is a custom LLM class that inherits from _LLMTemplate.
    It implements the generate_response method to provide custom generation logic.
    
    :param parameter1: Description of parameter1
    ...
    """
    def __init__(self, parameter1: str ...):
        super().__init__()
        # Add your custom initialization code here
        pass
        
        
    def generate_response(self, prompt: str) -> str:
        """
        Generates a response based on the input prompt.

        :param prompt: The input prompt to generate a response for
        :return: The generated response
        """ 

        # Implement your custom generation logic here
        pass
```
### 2. Add the new llm model to the 'LLMFactory' class in 'rag/generator/llm_handler.py'. (Modify the private method '__change_llm')
```python
class LLMFactory(_LLMTemplate):
    def __init__(self):
        pass

    
    def set_llm(self):
        pass

    
    # **kwargs are the parameters that will be passed to the llm (e.g. parameter1: str)
    def __change_llm(self, llm_name: str, **kwargs) -> None:
        """
        Change the llm according to the specified name.

        :param llm_name: Name of the llm to be set
        :param kwargs: Additional parameters for the llm
        :return: None
        """
        
        # Set the llm name
        self.llm_name = llm_name
        
        match llm_name:
            case "llm-name":
                self.llm = _LLMName(**kwargs)
                
    def generate_response(self):
        pass
```
### 3. Usage of the new llm model
```python
# Initial llm model must be a valid one
llm = LLMFactory("llm-name", parameter1="value1")
response = llm.generate_response(prompt="text to generate response for")

# If you want to change the llm model
llm.set_llm(llm_name="llm-name2", parameter1="value1")
response = llm.generate_response(prompt="text to generate response for")
```



---
# Configuration
### 1. Create a new class in 'config.py' which inherits from the base class '_ConfigTemplate'
```python
class ConfigName(_ConfigTemplate):
    """
    This is a custom config class that inherits from _ConfigTemplate.
    """

    def __init__(self) -> None:
        super().__init__(
            embedding_name="embedder-name",
            embedding_kwargs={"parameter1": "value1"},
            tokenizer_name="tokenizer-name",
            tokenizer_kwargs={"parameter1": "value1"},
            llm_name="llm-name",
            llm_kwargs={"parameter1": "value1"},
        )
```
### 2. Usage of the new config class
```python
from config import ConfigName
from rag.rag_entrypoint import process_document
from pymupdf import Document

# Create an instance of the custom config class
config = ConfigName()

# Read document from a file
doc = Document("path/to/document.pdf", filetype="pdf")

# Pass the config instance to the process_document function
process_document(conversation_id = 21, document=doc, config=config)
```



---
# Examples
TODO
---