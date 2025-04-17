from rag.llms.__llm_template import LLMTemplate
from openai import OpenAI


class ChatGPT(LLMTemplate):
    """
    ChatGPT class for generating text using the OpenAI API.
    This class is a wrapper around the OpenAI API for generating text.
    It uses the OpenAI API to generate text based on the provided prompt.

    :param llm_name: Name of the LLM
    :param initial_prompt: Initial prompt for the LLM
    :param api_key: API key for the OpenAI API
    """

    def __init__(self, llm_name: str, initial_prompt: str, api_key) -> None:
        super().__init__(llm_name)
        self.initial_prompt = initial_prompt
        self.client = OpenAI(api_key=api_key)


    def generate_response(self, prompt: str) -> str:
        """
        Generate a response based on the provided prompt using OpenAI API.

        :param prompt: The input prompt for the LLM
        :return: Generated response
        """

        # Generate a response using the OpenAI API
        response = self.client.responses.create(
            model = "gpt-3.5-turbo",
            instructions = self.initial_prompt,
            input = prompt,
        )

        # Extract the generated text from the response
        return response.output_text

