from pipelines.rag_test_pipeline import rag_test_pipeline

if __name__ == "__main__":
    # Run the RAG test pipeline
    rag_test_pipeline(
        document_path="/home/quuixlie/Desktop/Pan Tadeusz.pdf",
        query="Who is the father of Pan Tadeusz?",
        conversation_id=2137
    )