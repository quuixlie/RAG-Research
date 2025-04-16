from config import Config
from rag.rag_entrypoint import process_document, process_query
from pymupdf import Document

CONFIG = Config()

document = Document("/home/quuixlie/Desktop/100-English-Short-Stories.pdf", filetype="pdf")
# process_document(5, document, CONFIG)

queries = [ "What is the main theme of the story?", "What are the key events in the story?", "Who are the main characters?", "What is the setting of the story?", "What is the moral of the story?"]

for query in queries:
    print(f"Query: {query}")
    process_query(5, query, CONFIG)
    print("\n")