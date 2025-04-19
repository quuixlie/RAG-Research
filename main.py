from pipelines.rag_validation_pipeline import rag_validation_pipeline
from config import Config
import pandas as pd


def main():
    config = Config()

    # Load the dataset
    dataset = pd.read_csv("metrics/rag_dataset/dataset.csv")

    # Define the required columns
    required_columns = ["Question", "Answer", "FileNameRelativePath"]

    rag_validation_pipeline([config], dataset, required_columns, "metrics/rag_dataset/")


if __name__ == "__main__":
    main()