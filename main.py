from config import Config
from rag.rag_entrypoint import process_document, process_query
from rag.rag_source import remove_conversation
from pymupdf import Document
from rag.generator.prompt_builder import create_prompt
from rag.generator.llm_handler import LLMFactory


CONFIG = Config()
LLM = LLMFactory("OpenAI", **CONFIG.llm_kwargs)

document = Document("/home/quuixlie/Desktop/100-English-Short-Stories.pdf", filetype="pdf")
process_document(5, document, CONFIG)

queries = ["food poisoned", "food poisoned"]

for query in queries:
    print(f"Query: {query}")
    relevant_documents = process_query(5, query, CONFIG)
    prompt = create_prompt(query, relevant_documents)
    answer = LLM.generate_response(prompt)
    print(f"Prompt: {prompt}")
    print("\n\n\n\n")
    print(f"Answer: {answer}")
    print("\n\n\n")

remove_conversation(5)