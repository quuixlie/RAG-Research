from pipelines.rag_validation_pipeline import rag_validation_pipeline
from config import Config
from metrics.default_dataset import DefaultDataset, DatasetEntry
from rag.rag_architectures.rag_architecture_factory import RAGArchitectureFactory
from pymupdf import Document


def get_questions_from_file(questions:list[DatasetEntry],file_path:str) -> list[DatasetEntry]:
        return [x for x in questions if x.file_path == file_path]

def main():
    config = Config()
    dataset = DefaultDataset().load_data("dataset")
    # Leave only Pan Tadeusz.pdf from dataset
    dataset = get_questions_from_file(dataset, "dataset/TheLittlePrince.pdf")

    # for each file in dataset/ 
    # import os
    # for file in os.listdir("dataset"):
    #     if file.endswith(".pdf"):
    #         dataset2 = get_questions_from_file(dataset, "dataset/" + file)
    #         print(f"Processing {file}...")
    #         for entry in dataset2:
    #              print("    Question: ", entry.question)

    rag_validation_pipeline(
        configs=[config],
        dataset=dataset,
    )

if __name__ == "__main__":
    main()
