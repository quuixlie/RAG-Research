import json
from abc import ABC, abstractmethod
import httpx
from typing import Literal,get_args,override,Union
import openai

def get_args_recursive(t) -> list:
    """
    Parses the type annotations and returns all values as a flattened list
    """
    args = get_args(t)
    flat_args = []

    for arg in args:
        if getattr(arg, '__origin__', None) is Literal:
            flat_args.extend(get_args(arg))
        elif getattr(arg, '__origin__', None) is Union:
            flat_args.extend(get_args_recursive(arg))  # Recursive call
        else:
            flat_args.append(arg)

    return flat_args

OpenAIModelName = Literal['gpt-3.5-turbo','gpt-4']
OpenRouterModelName = Literal["deepseek/deepseek-r1-0528-qwen3-8b:free"]
LLMModelName = OpenAIModelName | OpenRouterModelName | Literal["speakleash/Bielik-11B-v2.2-Instruct"]

class LLM(ABC):
    """
    Base class for LLMs. This class defines the interface for LLMs, which are used to generate text.
    A new LLM can be created by inheriting from this class and implementing the generate_response method.

    :param llm_name: Name of the LLM
    """

    def __init__(self, 
                 model_name: LLMModelName,
                 temperature:float,
                 initial_prompt:str,
                 ):

        if temperature > 1 or temperature < 0:
            raise Exception(f"Invalid temperature: {temperature}. (the value must be between 0.0 and 1.0)")

        if model_name not in get_args_recursive(LLMModelName):
            raise Exception(f"Invalid model name: {model_name} (possible values are: {get_args_recursive(LLMModelName)})")

        self.model_name: LLMModelName = model_name
        self.temperature:float = temperature
        self.initial_prompt:str = initial_prompt

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

class BielikLLM(LLM):

    def __init__(self,
                 api_url:str,
                 llm_username:str,
                 llm_password:str,
                 temperature:float = 0.0,
                 initial_prompt:str = ""
                 ):
        """
        LLM hosted at Gdansk University of Technology

        Args:
            api_url (str): Base URL for requests
            llm_username (str): username to login to the API
            llm_username (str): password to login to the API

        Args
        """


        super().__init__("speakleash/Bielik-11B-v2.2-Instruct",temperature,initial_prompt)

        self.api_url = api_url
        self.llm_username:str = llm_username
        self.llm_password:str = llm_password

        self.temperature:float = temperature
        self.initial_prompt:str = initial_prompt

    @override
    def generate(self, prompt: str) -> str:
        data = {
            "messages": [
                {"role": "system", "content": self.initial_prompt},
                {"role": "user", "content": prompt}
            ],
            # "max_length": 16,  # adjust as needed
            "temperature": self.temperature
        }


        # verify=False -- disabling SSL verifiaction
        with httpx.Client(verify=False) as client:
            response = client.put(
                url=self.api_url,
                json=data,
                headers = {
                    "accept":"application/json",
                        "Content-Type":"application/json"
                },
                auth=(self.llm_username,self.llm_password),
            )

            response.raise_for_status()
            response_json = response.json()
            llm_response = response_json['response']

            return llm_response

    @override
    async def a_generate(self, prompt: str) -> str:
        data = {
            "messages": [
                {"role": "system", "content": self.initial_prompt},
                {"role": "user", "content": prompt}
            ],
            # "max_length": 16,  # adjust as needed
            "temperature": self.temperature
        }


        # verify=False -- disabling SSL verifiaction
        async with httpx.AsyncClient(verify=False) as client:
            response = await client.put(
                url=self.api_url,
                json=data,
                headers = {
                    "accept":"application/json",
                    "Content-Type":"application/json"
                },
                auth=(self.llm_username,self.llm_password),
            )

            response.raise_for_status()
            response_json = response.json()
            llm_response = response_json['response']

            return llm_response


class OpenRouterLLM(LLM):

    def __init__(self,
                 api_key:str,
                 model_name:OpenRouterModelName = "deepseek/deepseek-r1-0528-qwen3-8b:free",
                 temperature:float = 0.0,
                 initial_prompt:str = ""
                 ):
        super().__init__(model_name,temperature,initial_prompt)

        if model_name not in get_args(OpenRouterModelName):
            raise Exception(f"Invalid openai llm model name: {model_name} (possibel values are: {get_args(OpenRouterModelName)})")

        self.api_key = api_key

    @override
    def generate(self, prompt: str) -> str:
        data = {
            "model":self.model_name,
            "temperature": self.temperature,
            "messages": [
                {"role": "system", "content": self.initial_prompt},
                {"role": "user", "content": prompt}
            ],
        }

        with httpx.Client() as client:
            response = client.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                json=data,
                headers = {
                    "accept":"application/json",
                    "Content-Type":"application/json",
                    "Authorization":f"Bearer {self.api_key}"
                }
           )

            response.raise_for_status()
            llm_response = response.json()["choices"][0]["message"]["content"]
            return llm_response

    @override
    async def a_generate(self, prompt: str) -> str:

        data = {
            "model":self.model_name,
            "temperature": self.temperature,
            "messages": [
                {"role": "system", "content": self.initial_prompt},
                {"role": "user", "content": prompt}
            ],
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                json=data,
                headers = {
                    "accept":"application/json",
                    "Content-Type":"application/json",
                    "Authorization":f"Bearer {self.api_key}"
                }
           )

            response.raise_for_status()
            llm_response = response.json()["choices"][0]["message"]["content"]
            return llm_response





class OpenAILLM(LLM):

    def __init__(self,
                 api_key:str,
                 model_name: OpenAIModelName= 'gpt-3.5-turbo',
                 temperature:float = 0.0,
                 initial_prompt:str = ""
                 ):
        super().__init__(model_name,temperature,initial_prompt)

        if model_name not in get_args(OpenAIModelName):
            raise Exception(f"Invalid openai llm model name: {model_name} (possibel values are: {get_args(OpenAIModelName)})")

        self.client = openai.OpenAI(api_key=api_key)
        self.client_async = openai.AsyncOpenAI(api_key=api_key)

    @override
    def generate(self, prompt: str) -> str:

        response = self.client.chat.completions.create(
            messages=[
                {"role":"system","content":self.initial_prompt},
                {"role":"user","content":prompt}
            ],
            model = self.model_name,
        )

        model_response = response.choices[0].message.content

        if model_response is None:
            raise Exception("Something went wrong with generating model response")

        return model_response

    @override
    async def a_generate(self, prompt: str) -> str:

        response = await self.client_async.chat.completions.create(
            messages=[
                {"role":"system","content":self.initial_prompt},
                {"role":"user","content":prompt}
            ],
            model = self.model_name,
        )

        model_response = response.choices[0].message.content

        if model_response is None:
            raise Exception("Something went wrong with generating model response")

        return model_response

if __name__ == "__main__":
    import os


    ollm = OpenAILLM(
        api_key=os.getenv("OPENAI_API_KEY"),
        model_name="gpt-3.5-turbo",
        initial_prompt="You are a helpful assistant",
        temperature=0.0
    )

    openrouter = OpenRouterLLM(
        api_key=os.getenv("OPENROUTER_API_KEY"),
        model_name='deepseek/deepseek-r1-0528-qwen3-8b:free',
        initial_prompt="You are a helpful assistant",
        temperature=0.0
    )

    bielik = BielikLLM(
        api_url=os.getenv("PG_API_URL"),
        llm_username=os.getenv("PG_LLM_USERNAME"),
        llm_password=os.getenv("PG_LLM_PASSWORD"),
        temperature=0.0,
        initial_prompt="You are a helpful assistant"
    )

    openai_respnse = ollm.generate("Ile to 2 + 2 * 2")
    print("OpenAI response:",openai_respnse)

    bielik_response = bielik.generate("Ile to 2 + 2 * 2")
    print("Bielik response:",bielik_response)

    openrouter_response = openrouter.generate("Ile to 2 + 2 * 2")
    print("OPENROUTER response:",openrouter_response)






