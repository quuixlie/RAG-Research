from abc import ABC, abstractmethod
from deepeval.models import DeepEvalBaseLLM


class LLMTemplate(DeepEvalBaseLLM):
    """
    Base class for LLMs. This class defines the interface for LLMs, which are used to generate text.
    A new LLM can be created by inheriting from this class and implementing the generate_response method.
    The LLMTemplate class inherits from the DeepEvalBaseLLM class, which allows for the use of LLMs in the DeepEval framework.

    :param llm_name: Name of the LLM
    """

    def __init__(self, llm_name: str) -> None:
        self.llm_name = llm_name


    @abstractmethod
    def get_model_name(self) -> str:
        """
        Returns the name of the model. Function needed by the DeepEvalBaseLLM class.

        :return: Name of the model
        """
        return self.llm_name


    @abstractmethod
    def load_model(self):
        """
        Loads the model. This method should be implemented by the subclass. Function needed by the DeepEvalBaseLLM class.

        :return: The loaded model 
        """
        return None


    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generates a response from the model. This method should be implemented by the subclass.
        Function needed by the DeepEvalBaseLLM class.

        :param prompt: The prompt to generate a response for
        :return: The generated response
        """
        pass


    @abstractmethod
    async def a_generate(self, prompt: str) -> str:
        """
        Asynchronously generates a response from the model. This method should be implemented by the subclass.
        Function needed by the DeepEvalBaseLLM class.

        :param prompt: The prompt to generate a response for
        :return: The generated response
        """
        pass