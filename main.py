from pipelines.rag_validation_pipeline import rag_validation_pipeline
from config import Config
from rag.rag_architectures.rag_architecture_factory import RAGArchitectureFactory
from pymupdf import Document


def main():
    config = Config()
    rag_architecture = RAGArchitectureFactory(config.rag_architecture_name, config=config)

    doc = Document("TheLittlePrince.pdf")
    rag_architecture.process_document(
        conversation_id=1,
        document=doc
    )

    response = rag_architecture.process_query(
        conversation_id=1,
        query="What is the test document about?"
    )

    print("Response:", response)

    rag_architecture.get_rag_architecture().remove_conversation(1)



if __name__ == "__main__":
    main()