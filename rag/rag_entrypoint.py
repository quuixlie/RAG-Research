from config import ConfigTemplate
from rag.rag_source import *
from pymupdf import Document
from utils.document_parser import parse_to_markdown


def process_document(conversation_id: int, document: Document, config: ConfigTemplate) -> None:
        """
        Process the document to extract relevant information and store it in the vector database.

        :param conversation_id: ID of the conversation
        :param document: Document to be processed
        :param config: Configuration object containing RAG settings
        :return: None
        """

        # Prepare the vector database for the conversation
        prepare_vector_database(conversation_id, config)

        # Parse the document to markdown
        parsed_document_to_markdown = parse_to_markdown(document)

        # Embedding
        embeddings_with_text_pairs = prepare_document_embeddings_with_corresponding_text(parsed_document_to_markdown, config)
        store_embeddings_with_text_pairs(conversation_id, embeddings_with_text_pairs)


def process_query(conversation_id: int, query: str, config: ConfigTemplate) -> list:
    """
    Process the query to extract relevant information. Returns the most relevant document.

    :param conversation_id: ID of the conversation
    :param query: Query to be processed
    :param config: Configuration object containing RAG settings
    :return: List of relevant documents
    """

    # Process the query
    result = get_relevant_documents_by_query(conversation_id, query, config)

    return result
