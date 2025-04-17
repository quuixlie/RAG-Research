from config import Config
from rag.rag_architectures.rag_architecture_factory import RAGArchitectureFactory
from pymupdf import Document
import logging


document = Document("/home/quuixlie/Desktop/Pan Tadeusz.pdf", filetype="pdf")

config = Config()
classic_rag = RAGArchitectureFactory("classic-rag", config=config)

classic_rag.process_document(4, document)
print(classic_rag.process_query(4, "Who was food poisonned?"))
classic_rag.get_rag_architecture().remove_conversation(4)