from pipelines.rag_validation_pipeline import rag_validation_pipeline
from src.config import default_config 
from metrics.default_dataset import DefaultDataset, DatasetEntry
import os


def get_questions_from_file(questions:list[DatasetEntry],file_paths:list[str]) -> list[DatasetEntry]:
    return [x for x in questions if any([os.path.samefile(x.file_path, path) for path in file_paths])]

def main():
    config = default_config
    dataset = DefaultDataset().load_data("./dataset")
    print("Leaving only questions from TheLittlePrince.pdf")

    files =[
        "dataset/the_tell-tale_heart_0.pdf",
        "dataset/TheLittlePrince.pdf"
    ]

    dataset = get_questions_from_file(dataset, files);
    print("Filtered questions:",len(dataset))


    rag_validation_pipeline(
        configs=[config],
        dataset=dataset,
    )

if __name__ == "__main__":
    main()
