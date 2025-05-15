from pipelines.rag_validation_pipeline import rag_validation_pipeline
from config import Config
from metrics.default_dataset import DefaultDataset, DatasetEntry


def get_questions_from_file(questions:list[DatasetEntry],file_path:str) -> list[DatasetEntry]:
        return [x for x in questions if x.file_path == file_path]

def main():
    config = Config()
    dataset = DefaultDataset().load_data("dataset")
    # Leave only Pan Tadeusz.pdf from dataset
    dataset = get_questions_from_file(dataset, "dataset/TheLittlePrince.pdf")

    rag_validation_pipeline(
        configs=[config],
        dataset=dataset
    ) 

if __name__ == "__main__":
    main()
