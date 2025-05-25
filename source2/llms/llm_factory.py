# ============================ Models import ===========================
from .chat_gpt import ChatGPT
from .open_router import OpenRouter
# ======================================================================

from .__llm_template import LLMTemplate
import logging


class LLMFactory(LLMTemplate):
    """
    Factory class for creating LLMs. This class allows you to set the LLM model by calling the set_llm method
    with the desired LLM name. Then, you can use the generate_response method to generate text.
    You have to pass an existing LLM model and its parameters to the constructor.

    :param llm_name: Name of the LLM to be set
    :param kwargs: Additional parameters for the LLM model
    """

    def __init__(self, llm_name: str, **kwargs) -> None:
        super().__init__(llm_name)
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
        if self.llm_name != llm_name or self.__llm is None:
            self.__change_llm(llm_name, **kwargs)


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
            case "chat-gpt":
                self.__llm = ChatGPT(llm_name, **kwargs)
            case "open-router":
                self.__llm = OpenRouter(llm_name, **kwargs)
            case _:
                raise ValueError(f"Unsupported LLM name: {llm_name}. Please use a valid LLM name.")
        # ============================= Switch between models =============================


    def generate(self, prompt: str) -> str:
        """
        Generate a response based on the provided prompt.

        :param prompt: The input prompt for the LLM
        :return: Generated response
        """

        logging.info(f"Generating response for: \n{prompt}")

        # Generate response using the LLM
        response = self.__llm.generate(prompt)

        logging.info(f"Generated response: \n{response}")

        return response
    

    async def a_generate(self, prompt: str) -> str:
        """
        Asynchronously generate a response based on the provided prompt.

        :param prompt: The input prompt for the LLM
        :return: Generated response
        """

        logging.info(f"Generating async response for: \n{prompt}")

        # Generate async response using the LLM
        response = await self.__llm.a_generate(prompt)

        logging.info(f"Generated async response: \n{response}")

        return response
