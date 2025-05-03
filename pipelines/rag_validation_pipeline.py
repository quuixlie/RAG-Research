from metrics.full_evaluation import full_evaluate
from config import ConfigTemplate
from rag.rag_architectures.rag_architecture_factory import RAGArchitectureFactory
from metrics.dataset_template import DatasetTemplate
from database.vector_database import VectorDatabase
from pymupdf import Document


def __prepare_dataset(dataset: DatasetTemplate) -> DatasetTemplate:
    """
    Preprocess the dataset to ensure it is in the correct format.

    :param dataset: Dataset to preprocess.
    :return: Preprocessed dataset.
    """

    return dataset


def rag_validation_pipeline(configs: list[ConfigTemplate],
                            dataset: DatasetTemplate) -> None:
    """
    Validate the RAG architectures (entire RAG pipeline) on the provided dataset. It will save the results in the output/
    directory. Validation output for each configuration will be saved in a separate file, named same as the configuration class name.

    :param configs: List of configurations for the RAG architecture.
    :param dataset: Dataset to validate the RAG architectures on.
    """
    vector_database = VectorDatabase()

    total_accuracy = 0
    total_faithfulness = 0
    total_context_recall = 0
    total_context_precision = 0
    for config in configs:
        # Prepare the RAG architecture
        rag_architecture = RAGArchitectureFactory("classic-rag", config=config)

        file_path_relative_to_project_root = None
        current_row = 0
        # Iterate over the dataset and evaluate the RAG architecture on each file
        for row in dataset.data:
            question = row["question"]
            correct_answer = row["correct_answer"]
            relevant_contexts = row["relevant_contexts"]
            # If the file path is different from the previous one, process the new file
            if file_path_relative_to_project_root != row["file_path_relative_to_project_root"]:
                file_path_relative_to_project_root = row["file_path_relative_to_project_root"]
                
                # Load the file
                file = Document(file_path_relative_to_project_root)

                # Make sure the vector database is empty before processing a new file
                vector_database.remove_collection(2137)

                # Process the file 
                rag_architecture.process_document(2137, file)

        # Get RAG response to the question
        rag_response = rag_architecture.process_query(2137, question)
        rag_answer = rag_response["answer"]
        rag_contexts = rag_response["contexts"]

        # Evaluate the RAG architecture on the file
        accuracy, faithfulness, context_recall, context_precision = full_evaluate(
            question=question,
            correct_answer=correct_answer,
            relevant_contexts=relevant_contexts,
            rag_answer=rag_answer,
            rag_contexts=rag_contexts,
        )

        # Update the total metrics
        total_accuracy += accuracy
        total_faithfulness += faithfulness
        total_context_recall += context_recall
        total_context_precision += context_precision

        current_row += 1

        # Print total
        print("===================================================================")
        print(f"Total accuracy: {total_accuracy / current_row}")
        print(f"Total faithfulness: {total_faithfulness / current_row}")
        print(f"Total context recall: {total_context_recall / current_row}")
        print(f"Total context precision: {total_context_precision / current_row}")
        print(f"Current row: {current_row}")
        print(f"Current config: {config.__class__.__name__}")
        print()
        print(f"Question: {question}")
        print(f"Correct answer: {correct_answer}")
        print(f"RAG answer: {rag_answer}")
        print(f"Relevant contexts: {relevant_contexts}")
        print(f"RAG contexts: {rag_contexts}")
        print("===================================================================")

            