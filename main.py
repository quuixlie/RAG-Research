from pipelines.rag_validation_pipeline import rag_validation_pipeline
from config import Config
from metrics.default_dataset import DefaultDataset


def main():
    config = Config()
    dataset = DefaultDataset().load_data("./dataset")

    rag_validation_pipeline(
        configs=[config],
        dataset=dataset
    ) 

if __name__ == "__main__":
    main()
