# ============================ Architectures import ===========================
from .classic_rag import ClassicRAG
from .brain_rag import BrainRAG
from .knowledge_graph_rag import KGraphRAG
# =============================================================================


from typing import Literal
from .__rag_architecture import RAGArchitecture

import typing
if typing.TYPE_CHECKING:
    from ..config import Config

RAGArchitectureName = Literal["classic-rag","brain-rag","kg-rag"]

def rag_architecture_factory(config:'Config') -> RAGArchitecture:

    match config.rag_architecture_name:
        case "classic-rag":
            return ClassicRAG(config.rag_architecture_name,config)
        case "brain-rag":
            return BrainRAG(config.rag_architecture_name,config)
        case "kg-rag":
            return KGraphRAG(llm=config.llm,embedder=config.embedder,tokenizer=config.tokenizer,cross_encoder=config.cross_encoder,neo4j_uri=config.neo4j_uri,neo4j_user=config.neo4j_username,neo4j_password=config.neo4j_password)

    raise Exception("Unknown rag architecture: {}".format(config.rag_architecture_name))

