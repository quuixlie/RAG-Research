

def create_prompt(query: str, relevant_documents: list) -> str:
    """
    Create a prompt for the LLM based on the query and relevant documents.

    :param query: The user's query
    :param relevant_documents:
    :return: Formatted prompt string
    """

    prompt = f"Question: {query}\n\n"
    prompt += "Relevant documents:\n"
    prompt += __format_relevant_documents(relevant_documents)

    return prompt


def __format_relevant_documents(relevant_documents: list) -> str:
    """
    Format the relevant documents for the prompt.

    :param relevant_documents: List of relevant documents
    :return: Formatted string of relevant documents
    """

    formatted_docs = ""

    for i, doc in enumerate(relevant_documents):
        formatted_docs += f"\n================= Document {i + 1} =================\n{doc}"

    return formatted_docs
