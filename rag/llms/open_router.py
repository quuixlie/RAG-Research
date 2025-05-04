from rag.llms.__llm_template import LLMTemplate
from openai import OpenAI, AsyncOpenAI


class OpenRouter(LLMTemplate):
    """
    OpenRouter class for generating text using the OpenRouter API (it uses OpenAI API SDK).
    It uses the OpenRouter API to generate text based on the provided prompt.
    It inherits from the LLMTemplate class (DeepEvalBaseLLM).

    :param llm_name: Name of the LLM
    :param initial_prompt: Initial prompt for the LLM
    :param api_key: API key for the OpenAI API
    """

    def __init__(self, llm_name: str, initial_prompt: str, api_key: str, model_name: str) -> None:
        super().__init__(llm_name)
        self.initial_prompt = initial_prompt
        self.client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)
        self.async_client = AsyncOpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)
        self.model = model_name


    def get_model_name(self):
        """
        Returns the name of the model. Function needed by the DeepEvalBaseLLM class.

        :return: Name of the model
        """
        return super().get_model_name()
    

    def load_model(self):
        """
        Load the model. In this case, it is not necessary to load anything as the OpenRouter API is used.
        Function needed by the DeepEvalBaseLLM class.

        :return: None
        """
        return super().load_model()
    

    def generate(self, prompt: str) -> str:
        """
        Generate a response based on the provided prompt using OpenRouter API.

        :param prompt: The input prompt for the LLM
        :return: Generated response
        """

        # Generate a response using the OpenRouter API
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

         # Check if any error occurred
        if hasattr(response, "error") and response.error:
            response = response.error
        else:
            response = response.choices[0].message.content

        return response


    async def a_generate(self, prompt: str) -> str:
        """
        Generate an async response based on the provided prompt using OpenRouter API.

        :param prompt: The input prompt for the LLM
        :return: Generated response
        """

        # Generate a response using the OpenRouter API
        response = await self.async_client.chat.completions.create(
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

        # Check if any error occurred
        if hasattr(response, "error") and response.error:
            response = response.error
        else:
            response = response.choices[0].message.content

        return response