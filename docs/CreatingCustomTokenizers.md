# Creating a new tokenizer
This document describes how to create a new tokenizer in the RAG framework. The process involves creating a new class that inherits from the base class `TokenizerTemplate` and implementing the required methods. Below are the steps to create a new tokenizer.

---

## To create a new tokenizer, follow these steps:
### 1. Specify how you want to name your tokenizer, for example, `TokenizerName`.
### 2. Create a new file in the 'rag/tokenizers' directory with the name `tokenizer_name.py`.
### 3. Implement the tokenizer class in the new file (it should implement the `tokenize` method). For example:
```python
from rag.tokenizers.__tokenizer_template import TokenizerTemplate


class TokenizerName(TokenizerTemplate):
    """
    This is a custom tokenizer class that inherits from TokenizerTemplate.
    It implements the tokenize method to provide custom tokenization logic.
    
    :param tokenizer_name: Name of the tokenizer
    :param parameter1: Description of parameter1
    ...
    """
    def __init__(self, tokenizer_name: str, parameter1: str, ...) -> None:
        super().__init__(tokenizer_name)
        
        # Add your custom initialization code here
        self.parameter1 = parameter1
        
    def tokenize(self, text: str) -> list:
        """
        Tokenize the input text into chunks.
        
        :param text: The input text to tokenize
        :return: A list of tokenized chunks.
        """        
        # Implement your custom tokenization logic here
        pass
```
### 4. Go to the 'rag/tokenizers/tokenizer_factory.py' file and add your tokenizer to the `TokenizerFactory` class by importing the new tokenizer class and modifying the `__change_tokenizer` method:
```python
# ============================ Models import ===========================
from rag.tokenizers.tokenizer_name import TokenizerName
# ======================================================================

from rag.tokenizers.__tokenizer_template import TokenizerTemplate


class TokenizerFactory(TokenizerTemplate):
    """
    Factory class for creating tokenizers. This class allows you to set the tokenizer model by calling the set_tokenizer method
    with the desired tokenizer name. Then, you can use the tokenize method to tokenize text. You have to pass an existing
    tokenizer model and its parameters to the constructor.

    :param tokenizer_name: Name of the tokenizer to be set
    :param kwargs: Additional parameters for the tokenizer model
    """

    def __init__(self, tokenizer_name: str, **kwargs):
        pass 


    def set_tokenizer(self, tokenizer_name: str, **kwargs) -> None:
        pass 


    def __change_tokenizer(self, tokenizer_name: str, **kwargs) -> None:
        """
        Change the tokenizer according to the specified name.

        :param tokenizer_name: Name of the tokenizer to be set
        :return: None
        """

        # Set the tokenizer name
        self.tokenizer_name = tokenizer_name

        # ============================= Switch between models =============================
        match tokenizer_name:
            case "tokenizer-name":
                self.tokenizer = TokenizerName(tokenizer_name, **kwargs)
            case _:
                raise ValueError(f"Unsupported tokenizer name: {tokenizer_name}. Please use a valid tokenizer name.")
        # ============================= Switch between models =============================


    def tokenize(self, text: str) -> list:
        pass 
```
## Usage of the new tokenizer
```python
# Initial tokenizer must be a valid one
from rag.tokenizers.tokenizer_factory import TokenizerFactory

# Create a new tokenizer
tokenizer = TokenizerFactory(tokenizer_name="tokenizer-name", parameter1="value1")
fragments = tokenizer.tokenize(text="text to tokenize")

# If you want to change the tokenizer
tokenizer.set_tokenizer(tokenizer_name="tokenizer-name2", parameter1="value1")
fragments = tokenizer.tokenize(text="text to tokenize")
```