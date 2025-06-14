from src.architectures.rag_architecture_factory import rag_architecture_factory
from src.config import Config
from pymupdf import Document


def rag_test_pipeline(document_path: str, query: str, conversation_id: int, config: Config) -> None:
    document = Document(document_path, filetype="pdf")
    classic_rag = rag_architecture_factory(config=config)
    classic_rag.process_document(conversation_id, document)
    print(classic_rag.process_query(conversation_id, query))
    classic_rag.remove_conversation(conversation_id)
