from abc import ABC, abstractmethod


class LLMTemplate(ABC):
    """
    Base class for LLMs. This class defines the interface for LLMs, which are used to generate text.
    A new LLM can be created by inheriting from this class and implementing the generate_response method.

    :param llm_name: Name of the LLM
    """

    def __init__(self, llm_name: str) -> None:
        self.llm_name = llm_name


    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        """
        Generate a response based on the provided prompt.

        :param prompt: The input prompt for the LLM
        :return: Generated response
        """
        pass