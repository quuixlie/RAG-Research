from rag.llms.__llm_template import LLMTemplate
from openai import OpenAI


class OpenRouter(LLMTemplate):
    """
    OpenRouter class for generating text using the OpenRouter API (it uses OpenAI API SDK).
    It uses the OpenRouter API to generate text based on the provided prompt.

    :param llm_name: Name of the LLM
    :param initial_prompt: Initial prompt for the LLM
    :param api_key: API key for the OpenAI API
    """

    def __init__(self, llm_name: str, initial_prompt: str, api_key: str, model_name: str) -> None:
        super().__init__(llm_name)
        self.initial_prompt = initial_prompt
        self.client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)
        self.model = model_name


    def generate_response(self, prompt: str) -> str:
        """
        Generate a response based on the provided prompt using OpenAI API.

        :param prompt: The input prompt for the LLM
        :return: Generated response
        """

        # Generate a response using the OpenAI API
        response = self.client.chat.completions.create(
            model=self.model,
            messages= [
                {
                    "role": "system",
                    "content": self.initial_prompt
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        # Extract the generated text from the response
        return response.choices[0].message.content

