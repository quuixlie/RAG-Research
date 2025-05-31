from pydantic import BaseModel
from pydantic.fields import Field
from .chat_gpt import ChatGPT
from .open_router import OpenRouter
from typing import Literal, Optional,Annotated,get_args
from .llm import LLM
import logging


LLMType = Literal["openai","open-router"]
OpenAIModelName = Literal["gpt-3.5-turbo","gpt-4"]
OpenRouterModelName = Literal["deepseek/deepseek-r1-0528-qwen3-8b:free"]
LLMModelName = OpenAIModelName | OpenRouterModelName

class LLMKwargs(BaseModel):
    api_key:Optional[str] = None
    initial_prompt:Optional[str] = None
    model_name: LLMModelName = "deepseek/deepseek-r1-0528-qwen3-8b:free"
    temperature: Annotated[float, Field(ge=0.0,le=1.0)] = 0.0


def llm_factory(llm_type:LLMType,kwargs: LLMKwargs) -> LLM:
    logging.info(f"Creating LLM from type: {llm_type} and model: {kwargs.model_name}")
    match llm_type:

        case "openai":

            if kwargs.model_name not in get_args(OpenAIModelName):
                logging.error("| llm_factory | Wrong model specified for openai LLM: {}, Available models are: ".format(kwargs.model_name,get_args(OpenAIModelName)))
                exit(-1)

            if kwargs.api_key is None:
                logging.error("| llm_factory | No API_KEY specified for chat-gpt LLM")
                exit(-1)

            return ChatGPT(llm_name=kwargs.model_name,initial_prompt=kwargs.initial_prompt, api_key=kwargs.api_key,model_name=kwargs.model_name,temperature=kwargs.temperature)

        case "open-router":

            if kwargs.model_name not in get_args(OpenRouterModelName):
                logging.error("| llm_factory | Wrong model specified for open-router LLM: {}, Available models are: {}".format(kwargs.model_name,get_args(OpenRouterModelName)))
                exit(-1)

            if kwargs.api_key is None:
                logging.error("| llm_factory | No API_KEY specified for open-router LLM")
                exit(-1)

            return OpenRouter(llm_name=kwargs.model_name,initial_prompt=kwargs.initial_prompt,api_key=kwargs.api_key,model_name=kwargs.model_name)

        case _:
            raise ValueError(f"Unsupported LLM type: {llm_type}. Please use a valid LLM name.")
