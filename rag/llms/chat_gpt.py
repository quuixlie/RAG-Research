from rag.llms.__llm_template import LLMTemplate
from openai import OpenAI, AsyncOpenAI


class ChatGPT(LLMTemplate):
    """
    ChatGPT class for generating text using the OpenAI API.
    This class is a wrapper around the OpenAI API for generating text.
    It uses the OpenAI API to generate text based on the provided prompt.
    It inherits from the LLMTemplate class (DeepEvalBaseLLM).

    :param llm_name: Name of the LLM
    :param initial_prompt: Initial prompt for the LLM
    :param api_key: API key for the OpenAI API
    """

    def __init__(self, llm_name: str, initial_prompt: str, api_key: str, model: str) -> None:
        super().__init__(llm_name)
        self.initial_prompt = initial_prompt
        self.client = OpenAI(api_key=api_key)
        self.async_client = AsyncOpenAI(api_key=api_key)
        self.model = model


    def get_model_name(self):
        """
        Returns the name of the model. Function needed by the DeepEvalBaseLLM class.

        :return: Name of the model
        """
        return super().get_model_name()
    

    def load_model(self):
        """
        Load the model. In this case, it is not necessary to load anything as the OpenAI API is used.
        Function needed by the DeepEvalBaseLLM class.

        :return: None
        """
        return super().load_model()
    

    def generate(self, prompt: str) -> str:
        """
        Generate a response based on the provided prompt using OpenAI API.

        :param prompt: The input prompt for the LLM
        :return: Generated response
        """

        try:
            # Generate a response using the OpenAI API
            response = self.client.responses.create(
                model = self.model,
                instructions = self.initial_prompt,
                input = prompt,
            )
            response = response.output_text
        except Exception as e: # Return error
            response = e

        return response


    async def a_generate(self, prompt: str) -> str:
        """
        Generate an async response based on the provided prompt using OpenAI API.

        :param prompt: The input prompt for the LLM
        :return: generated response
        """

        try:
            response = self.async_client.responses.create(
                model = self.model,
                instructions=self.initial_prompt,
                input = prompt,
            )
            response = response.output_text
        except Exception as e: # Return error
            response = e

        return response