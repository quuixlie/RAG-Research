# ============================ Architectures import ===========================
from .classic_rag import ClassicRAG
from .brain_rag import BrainRAG
# =============================================================================


from typing import Literal
from .__rag_architecture import RAGArchitecture

import typing
if typing.TYPE_CHECKING:
    from ..config import Config

RAGArchitectureName = Literal["classic-rag","brain-rag"]

def rag_architecture_factory(config:'Config') -> RAGArchitecture:

    match config.rag_architecture_name:
        case "classic-rag":
            return ClassicRAG(config.rag_architecture_name,config)
        case "brain-rag":
            return BrainRAG(config.rag_architecture_name,config)

    raise Exception("Unknown rag architecture: {}".format(config.rag_architecture_name))

