from rag.llms.llm_factory import LLMFactory

def contextual_precision(
    question: str,
    relevant_contexts: list[str],
    rag_contexts: list[str],
    llm: LLMFactory
) -> float:
    """
    Evaluate the context precision of the RAG system (synchronous version).

    Args:
        question (str): The question asked.
        relevant_contexts (list[str]): A list of ground truth relevant contexts.
        rag_contexts (list[str]): The list of contexts retrieved by the RAG system.
        llm (LLMFactory): The LLM to use for evaluation.

    Returns:
        float: The context precision score (between 0.0 and 1.0).
    """

    if not rag_contexts:
        return 0.0  # If no contexts are retrieved, precision is 0

    num_retrieved = len(rag_contexts)
    num_relevant_retrieved = 0

    for i, context in enumerate(rag_contexts):
        prompt = f"""You are an expert evaluator tasked with determining the relevance of a document to a given question.

        Given the following:

        - Question: {question}
        - Retrieved Document: {context}

        Is the Retrieved Document relevant to answering the Question? Explain your reasoning. Respond with 'yes' if it is relevant, and 'no' if it is not.
        """
        try:
            response = llm.generate(prompt)
            if "yes" in response.lower():
                num_relevant_retrieved += 1
        except Exception as e:
            print(f"Error evaluating relevance for context {i+1}: {e}")

    context_precision = num_relevant_retrieved / num_retrieved if num_retrieved > 0 else 0.0
    return context_precision