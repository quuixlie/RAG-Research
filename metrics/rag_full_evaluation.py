import os

from rag.rag_architectures.rag_architecture_factory import RAGArchitectureFactory
from config import ConfigTemplate, Config
import pandas as pd
from database.vector_database import VectorDatabase
from pymupdf import Document
import logging


def __check_dataset_columns(dataset: pd.DataFrame, required_columns: list) -> None:
    """
    Check if the dataset contains the required columns.

    :param dataset: Dataset to check.
    :param required_columns: List of required columns. First column should contain the question, second column should contain
    # the answer, and third column should contain the relative path to the file.
    :raises ValueError: If any required column is missing.
    """
    for column in required_columns:
        if column not in dataset.columns:
            raise ValueError(f"Dataset must contain the column: {column}")


def prepare_dataset(dataset: pd.DataFrame, required_columns: list) -> pd.DataFrame:
    """
    Preprocess the dataset to ensure it is in the correct format.

    :param dataset: Dataset to preprocess.
    :param required_columns: List of required columns. First column should contain the question, second column should contain
    # the answer, and third column should contain the relative path to the file.
    :return: Preprocessed dataset.
    """

    # Check if the dataset contains the required columns
    __check_dataset_columns(dataset, required_columns)

    # Drop unnecessary columns
    dataset = dataset[required_columns]

    dataset = dataset.dropna()  # Drop rows with missing values
    dataset = dataset.reset_index(drop=True)  # Reset index after dropping rows

    # Sort dataset by filename paths to ensure that the same files are processed one after another
    dataset = dataset.sort_values(by=[required_columns[2]])

    return dataset


def __evaluate_rag_on_file(rag_architecture: RAGArchitectureFactory, file: Document, question_answer_pairs: list, vector_database: VectorDatabase,
                           output_filename: str) -> None:
    """
    Evaluate the RAG architecture on a single file.

    :param rag_architecture: RAG architecture to evaluate.
    :param file: File to evaluate.
    :param question_answer_pairs: List of question-answer pairs for the file.
    :param vector_database: Vector database instance. Will be used to clear collections after processing each file.
    """

    logging.info(f"Processing file: {file.name}")

    # Create the output directory if it doesn't exist
    if not os.path.exists("output/"):
        os.makedirs(os.path.dirname("output/"), exist_ok=True)
        logging.info(f"Output directory does not exist: output/, creating it...")

    output_file = open(f"output/{output_filename}.txt", "a")
    try:  # Ensure that the vector database is cleared after processing each file
        rag_architecture.process_document(2137, file)

        logging.info(f"Number of question-answer pairs: {len(question_answer_pairs)}")

        for question, correct_answer in question_answer_pairs:
            rag_answer = rag_architecture.process_query(2137, question)

            # Log the evaluation results
            logging.info('=' * 50)
            logging.info(f"Evaluating question: {question}")
            logging.info(f"RAG answer: {rag_answer}")
            logging.info(f"Correct answer: {correct_answer}")
            logging.info('=' * 50)

            # Write the evaluation results to the output file
            output_file.write(f"Question: {question}, RAG answer: {rag_answer}, Correct answer: {correct_answer}\n")
    except Exception as e:
        logging.error(f"Error processing file {file.name}: {e}")
    finally:
        if vector_database.has_collection(2137):
            vector_database.remove_collection(2137)
        output_file.close()


def evaluate_rag_full(configs: list[ConfigTemplate], dataset: pd.DataFrame, required_columns: list, dataset_directory_path: str) -> None:
    """
    Evaluate the RAG architectures (entire RAG pipeline) on the provided dataset.

    :param configs: List of configurations for the RAG architecture.
    :param required_columns: List of required columns. First column should contain the question, second column should contain
    # the answer, and third column should contain the relative path to the file.
    :param dataset_directory_path: Path to the directory containing the dataset files. Relative
    :param dataset: Dataset to evaluate the RAG architectures on.
    """
    # Initialize the vector database to remove conversations after each document
    vector_database = VectorDatabase()

    # Prepare the dataset for evaluation
    dataset = prepare_dataset(dataset, required_columns)

    # Get the unique filenames from the dataset to avoid reprocessing the same files
    unique_files = dataset[required_columns[2]].unique()

    for config in configs:
        # Initialize the RAG architecture to be evaluated
        rag_architecture = RAGArchitectureFactory(config.rag_architecture_name, config=config)

        for file in unique_files:
            question_answer_pairs = dataset[dataset[required_columns[2]] == file][
                [required_columns[0], required_columns[1]]].values.tolist()

            file = Document(dataset_directory_path + file)
            __evaluate_rag_on_file(rag_architecture, file, question_answer_pairs, vector_database, config.__class__.__name__)