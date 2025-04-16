from database.vector_database import VectorDatabase
from config import ConfigTemplate
from rag.retriever.tokenzier import TokenizerFactory
from rag.retriever.embedder import EmbedderFactory


# Keep vector database instance in memory to avoid reloading it every time (For performance)
VECTOR_DATABASE = VectorDatabase()
TOKENIZER_FACTORY = TokenizerFactory("fixed-size", chunk_size=256)
EMBEDDER_FACTORY = EmbedderFactory("sentence-transformers/all-MiniLM-L12-v2")


def prepare_vector_database(conversation_id: int, config: ConfigTemplate) -> None:
    """
    Prepare the vector database for a conversation by creating a collection if it doesn't exist.

    :param conversation_id: ID of the conversation
    :param config: Configuration object containing vector database settings
    :return: None
    """

    # Create a collection for the conversation if it doesn't exist
    if not VECTOR_DATABASE.has_collection(conversation_id):
        VECTOR_DATABASE.create_collection(conversation_id, dimension=config.embedding_kwargs["dimension"])


def remove_vector_database(conversation_id: int) -> None:
    """
    Remove the vector database collection for a conversation if it exists.

    :param conversation_id: ID of the conversation
    :return: None
    """

    if VECTOR_DATABASE.has_collection(conversation_id):
        VECTOR_DATABASE.remove_collection(conversation_id)


def prepare_document_embeddings_with_corresponding_text(document: str, config: ConfigTemplate) -> list:
    """
    Prepare document embeddings by splitting the document into fragments and vectorizing them.

    :param document: Document to be embedded
    :param config: Configuration object containing vector database settings
    :return: List of document fragments
    """

    # Split the document into fragments
    TOKENIZER_FACTORY.set_tokenizer(config.tokenizer_name, **config.tokenizer_kwargs)
    fragments = TOKENIZER_FACTORY.tokenize(document)

    EMBEDDER_FACTORY.set_embedder(config.embedding_model, **config.embedding_kwargs)
    embeddings = EMBEDDER_FACTORY.encode(fragments, show_progress_bar=True)

    # Create a list of dictionaries with text and embedding
    embeddings_with_text_pairs = [
        {
            "text": fragment,
            "embedding": embedding.tolist()
        } for fragment, embedding in zip(fragments, embeddings)
    ]

    return embeddings_with_text_pairs


def store_embeddings_with_text_pairs(conversation_id: int, data: list) -> None:
    """
    Store the embeddings with their corresponding text in the vector database.

    :param conversation_id: ID of the conversation
    :param data: List of tuples containing embeddings and their corresponding text
    :return: None
    """

    VECTOR_DATABASE.insert_data(conversation_id, data)