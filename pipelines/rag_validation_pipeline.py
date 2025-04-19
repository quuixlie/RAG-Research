from metrics.rag_full_evaluation import evaluate_rag_full
from config import ConfigTemplate
import pandas as pd


def rag_validation_pipeline(configs: list[ConfigTemplate],
                            dataset: pd.DataFrame,
                            required_columns: list,
                            dataset_directory_path: str) -> None:
    """
    Validate the RAG architectures (entire RAG pipeline) on the provided dataset. It will save the results in the output/
    directory. Validation output for each configuration will be saved in a separate file, named same as the configuration class name.

    :param configs: List of configurations for the RAG architecture.
    :param required_columns: List of required columns. First column should contain the question, second column should contain
    # the answer, and third column should contain the relative path to the file.
    :param dataset_directory_path: Path to the directory containing the dataset files. Relative
    :param dataset: Dataset to validate the RAG architectures on.
    """

    evaluate_rag_full(configs, dataset, required_columns, dataset_directory_path)