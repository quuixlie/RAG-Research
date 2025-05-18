from typing import List
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from rag.embedders.embedder_factory import EmbedderFactory


def context_recall(
    relevant_contexts: List[str], 
    rag_contexts: List[str], 
    similarity_threshold: float = 0.8,
    embedder_name: str = "basic-embedder",
    embedder_kwargs: dict = {
        "sentence_transformer_name": "mixedbread-ai/mxbai-embed-large-v1",
        "device": "cpu", 
    }
) -> float:
    """
    Evaluate context recall: the proportion of relevant contexts for which
    at least one semantically similar context was found among rag_contexts.

    Args:
        relevant_contexts (List[str]): Ground truth contexts.
        rag_contexts (List[str]): Retrieved/generated contexts.
        similarity_threshold (float): Cosine similarity threshold to count a match.
        embedder_name (str): Name of the embedder to use for generating embeddings.
        embedder_kwargs (dict): Additional arguments for the embedder.

    Returns:
        float: Recall score between 0.0 and 1.0.
    """
    if not relevant_contexts:
        print("No relevant contexts provided.")
        return 0.0
    if not rag_contexts:
        print("No RAG contexts provided.")
        return 0.0

    # GPU memory limit pass
    embedder = EmbedderFactory(embedder_name, **embedder_kwargs)

    try:
        relevant_embeddings = np.array(embedder.encode(relevant_contexts))
        rag_embeddings = np.array(embedder.encode(rag_contexts))
    except Exception as e:
        print(f"Error generating embeddings: {e}")
        return 0.0

    if relevant_embeddings.ndim == 1:
        relevant_embeddings = relevant_embeddings.reshape(1, -1)
    if rag_embeddings.ndim == 1:
        rag_embeddings = rag_embeddings.reshape(1, -1)

    recalled_count = 0

    print("Relevant contexts:")
    for context in relevant_contexts:
        print(f"  {context}")

    for relevant_vec in relevant_embeddings:
        similarities = cosine_similarity(relevant_vec.reshape(1, -1), rag_embeddings)
        print(f"Similarities: {similarities}")
        if np.any(similarities >= similarity_threshold):
            recalled_count += 1

    return recalled_count / len(relevant_contexts)
