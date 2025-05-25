from config import ConfigTemplate
from source.rag_architectures.rag_architecture_factory import RAGArchitectureFactory
from pymupdf import Document


def rag_test_pipeline(document_path: str, query: str, conversation_id: int, config: ConfigTemplate) -> None:
    document = Document(document_path, filetype="pdf")

    classic_rag = RAGArchitectureFactory(config.rag_architecture_name, config=config)

    classic_rag.process_document(conversation_id, document)

    print(classic_rag.process_query(conversation_id, query))

    classic_rag.get_rag_architecture().remove_conversation(conversation_id)
