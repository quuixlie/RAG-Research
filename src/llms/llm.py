from abc import ABC, abstractmethod


class LLM(ABC):
    """
    Base class for LLMs. This class defines the interface for LLMs, which are used to generate text.
    A new LLM can be created by inheriting from this class and implementing the generate_response method.

    :param llm_name: Name of the LLM
    """

    def __init__(self, llm_name: str) -> None:
        self.llm_name = llm_name

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generates a response from the model. This method should be implemented by the subclass.

        :param prompt: The prompt to generate a response for
        :return: The generated response or None in case of error
        """
        pass


    @abstractmethod
    async def a_generate(self, prompt: str) -> str:
        """
        Asynchronously generates a response from the model. This method should be implemented by the subclass.

        :param prompt: The prompt to generate a response for
        :return: The generated response or None in case of error
        """
        pass

