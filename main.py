from config import Config
from rag.rag_architectures.rag_architecture_factory import RAGArchitectureFactory
from pymupdf import Document


document = Document("/home/quuixlie/Desktop/Pan Tadeusz.pdf", filetype="pdf")

config = Config()
classic_rag = RAGArchitectureFactory(config.rag_architecture_name, config=config)

classic_rag.process_document(5, document)
print(classic_rag.process_query(5, "Who was the father of Pan Tadeusz?"))
classic_rag.get_rag_architecture().remove_conversation(5)