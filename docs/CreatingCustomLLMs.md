# Creating a new LLM
This document describes how to create a new LLM in the RAG framework. The process involves creating a new class that inherits from the base class `LLMTemplate` and implementing the required methods. Below are the steps to create a new LLM.

---

## To create a new LLM, follow these steps:
### 1. Specify how you want to name your LLM, for example, `LLMName`.
### 2. Create a new file in the 'rag/llms' directory with the name `llm_name.py`.
### 3. Implement the LLM class in the new file (it should implement the `generate_response` method). For example:
```python
from rag.llms.__llm_template import LLMTemplate


class LLMName(LLMTemplate):
    """
    This is a custom LLM class that inherits from LLMTemplate.
    It implements the generate_response method to provide custom response generation logic.
    
    :param llm_name: Name of the LLM
    :param parameter1: Description of parameter1
    ...
    """
    def __init__(self, llm_name: str, parameter1: str, ...) -> None:
        super().__init__(llm_name)
        
        # Add your custom initialization code here
        self.parameter1 = parameter1
        
    def generate_response(self, prompt: str) -> str:
        """
        Generate a response based on the input prompt.
        
        :param prompt: The input prompt to generate a response for
        :return: The generated response.
        """        
        # Implement your custom response generation logic here
        pass
```
### 4. Go to the 'rag/llms/llm_factory.py' file and add your LLM to the `LLMFactory` class by importing the new LLM class and modifying the `__change_llm` method:
```python
# ============================ Models import ===========================
from rag.llms.llm_name import LLMName
# ======================================================================

from rag.llms.__llm_template import LLMTemplate


class LLMFactory(LLMTemplate):
    """
    Factory class for creating LLMs. This class allows you to set the LLM model by calling the set_llm method
    with the desired LLM name. Then, you can use the generate_response method to generate text.
    You have to pass an existing LLM model and its parameters to the constructor.

    :param llm_name: Name of the LLM to be set
    :param kwargs: Additional parameters for the LLM model
    """

    def __init__(self, llm_name: str, **kwargs) -> None:
        pass 


    def set_llm(self, llm_name: str, **kwargs) -> None:
        pass


    def __change_llm(self, llm_name: str, **kwargs) -> None:
        """
        Change the LLM according to the specified name.

        :param llm_name: Name of the LLM to be set
        :return: None
        """

        # Set the LLM name
        self.llm_name = llm_name

        # ============================= Switch between models =============================
        match llm_name:
            case "llm_name":
                self.llm = LLMName(llm_name, **kwargs)
            case _:
                raise ValueError(f"Unsupported LLM name: {llm_name}. Please use a valid LLM name.")
        # ============================= Switch between models =============================


    def generate_response(self, prompt: str) -> str:
        pass 
```
## Usage of the new LLM
```python
from rag.llms.llm_factory import LLMFactory

# Create a new LLM
llm = LLMFactory("llm_name", parameter1="value1")
response = llm.generate_response("What is the capital of France?")

# If you want to change the LLM
llm.set_llm("llm_name2", parameter1="value1")
```