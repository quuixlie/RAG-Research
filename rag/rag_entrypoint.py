from config import ConfigTemplate
from rag.rag_source import *
from pymupdf import Document
from utils.document_parser import parse_to_markdown


def process_document(conversation_id: int, document: Document, config: ConfigTemplate) -> None:
        # Prepare the vector database for the conversation
        prepare_vector_database(conversation_id, config)

        # Parse the document to markdown
        parsed_document_to_markdown = parse_to_markdown(document)

        # Embedding
        embeddings_with_text_pairs = prepare_document_embeddings_with_corresponding_text(parsed_document_to_markdown, config)
        store_embeddings_with_text_pairs(conversation_id, embeddings_with_text_pairs)

        remove_vector_database(conversation_id)
