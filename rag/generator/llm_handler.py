import os
from abc import ABC, abstractmethod
import openai
from openai import OpenAI


class _LLMTemplate(ABC):
    """
    Abstract base class for LLM.
    """

    def __init__(self):
        self.llm_name = None


    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generate a response based on the provided prompt.

        :param prompt: The input prompt for the LLM
        :return: Generated response
        """
        pass



class LLMFactory(_LLMTemplate):
    """
    Factory class for creating LLMs.
    Set the LLM model by calling the set_llm method with the desired LLM name.
    Then, you can use the generate method to generate text.

    :param llm_name: Name of the LLM to be set
    """

    def __init__(self, llm_name: str, **kwargs):
        super().__init__()
        self.__llm = None
        self.set_llm(llm_name, **kwargs)


    def set_llm(self, llm_name: str, **kwargs) -> None:
        """
        Set the LLM name and change the LLM model.
        (If the new LLM name is different from the current one, change the LLM model)

        :param llm_name: Name of the LLM to be set
        :return: None
        """

        # If the new LLM name is different from the current one, change the LLM (model)
        if self.llm_name != llm_name:
            self.__change_llm(llm_name, **kwargs)


    def __change_llm(self, llm_name: str, **kwargs) -> None:
        """
        Change the LLM according to the specified name.

        :param llm_name: Name of the LLM to be set
        :return: None
        """

        # Set the LLM name
        self.llm_name = llm_name

        match llm_name:
            case "OpenAI":
                self.__llm = _OpenAILLM(**kwargs)
            case _:
                raise ValueError(f"LLM {llm_name} not supported.")


    def generate(self, prompt: str) -> str:
        """
        Generate a response based on the provided prompt.

        :param prompt: The input prompt for the LLM
        :return: Generated response
        """

        # Check if the LLM is set
        if self.__llm is None:
            raise ValueError("LLM not set. Please set the LLM before generating text.")

        # Generate text using the LLM
        return self.__llm.generate(prompt)


class _OpenAILLM(_LLMTemplate):
    """
    OpenAI LLM class for generating text using the OpenAI API.
    """

    def __init__(self, api_key: str):
        super().__init__()
        self.api_key = api_key
        self.client = OpenAI(api_key=self.api_key)


    def generate(self, prompt: str) -> str:
        """
        Generate a response based on the provided prompt using OpenAI API.

        :param prompt: The input prompt for the LLM
        :return: Generated response
        """

        # Generate a response using the OpenAI API
        response = self.client.responses.create(
            model = "gpt-3.5-turbo",
            instructions = "You are a helpful assistant.",
            input = prompt,
        )

        # Extract the generated text from the response
        return response.output_text