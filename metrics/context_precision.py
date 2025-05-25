from source.llms.llm_factory import LLMFactory


def context_precision(question: str, rag_contexts: list[str], correct_answer: str, llm: LLMFactory, async_generate: bool = False) -> float:
    """
    Evaluate the context precision of the RAG system using the LLM.

    Args:
        question (str): The question asked.
        rag_contexts (list[str]): The contexts used by the RAG architecture to generate the answer.
        correct_answer (str): The correct answer to the question.
        llm (LLMFactory): The LLM to use for evaluation.
    async_generate (bool): Whether to use async evaluation.
    Returns:
        float: The context precision score.
    """
    if len(rag_contexts) == 0 or question == "":
        print("No contexts provided for evaluation or question is empty.")
        return 0.0

    relevant_count = 0
    irrelevant_count = 0
    for context in rag_contexts:
        prompt = f"""You are an expert evaluator tasked with verifying the correctness of answers.
        Given the following:
        - Question: {question}
        - Context: {context}
        - Correct Answer: {correct_answer}
        Determine whether the context is relevant to the question. Include your reasoning in your response.
        """

        response = None
        if async_generate:
            response = llm.a_generate(prompt)
        else:
            response = llm.generate(prompt)

        # Check if context is relevant to the question
        prompt = f"""
        You are a factual evaluator.
        Given the following:
        - Question: {question}
        - Reasoning: {response}
        Respond with exactly "yes" if the reasoning justifies that the context is relevant to the question. Respond with exactly "no" if the reasoning shows that the context is irrelevant or insufficient. Do not output anything else.
        """
        if async_generate:
            response = llm.a_generate(prompt)
        else:
            response = llm.generate(prompt)

        # Parse the response
        try:
            if response.lower() == "yes":
                relevant_count += 1
            elif response.lower() == "no":
                irrelevant_count += 1
        except Exception as e:
            print(f"Error parsing response: {e}")
            # Wait if error occurs
            input("Do you want to continue? (y/n): ")
            irrelevant_count += 1

    # Calculate the contextual precision score
    total_count = relevant_count + irrelevant_count
    if total_count == 0:
        return 0.0
    else:
        precision_score = relevant_count / total_count
        return precision_score
