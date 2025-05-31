# from langchain.retrievers.document_compressors.cross_encoder import BaseCrossEncoder
# ============================ Models import ===========================
from .basic_cross_encoder import BasicCrossEncoder
# ======================================================================

from typing import Literal
from .cross_encoder import CrossEncoder
from pydantic import BaseModel

CrossEncoderName = Literal["cross-encoder/ms-marco-MiniLM-L-6-v2"]

class CrossEncoderKwargs(BaseModel):
    model_name:CrossEncoderName = "cross-encoder/ms-marco-MiniLM-L-6-v2"
    device: Literal["cpu", "cuda"] = "cuda"

def cross_encoder_factory(name:CrossEncoderName,kwargs:CrossEncoderKwargs = CrossEncoderKwargs()) -> CrossEncoder:

    match name:
        case "cross-encoder/ms-marco-MiniLM-L-6-v2":
            return BasicCrossEncoder(cross_encoder_name=name,sentence_transformer_name=kwargs.model_name,device=kwargs.device)

    raise Exception("Invalid cross_encoder name: {}".format(name))




