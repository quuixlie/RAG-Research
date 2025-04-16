from config import Config
from rag.rag_entrypoint import process_document
from pymupdf import Document

CONFIG = Config()

document = Document("/home/quuixlie/Desktop/100-English-Short-Stories.pdf", filetype="pdf")
process_document(5, document, CONFIG)