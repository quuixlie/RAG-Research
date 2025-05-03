from abc import ABC


class DatasetTemplate(ABC):
    """
    Abstract class for the dataset template. It defines the structure of the dataset and the methods to be implemented by
    subclasses. Rows should be sorted by file_path_relative_to_project_root, so that the same file is processed by RAG only once.
    """
    data = [
        {
            "question": "",
            "correct_answer": "",
            "relevant_contexts": [
               "",
            ],
            "file_path_relative_to_project_root": ""
        },
    ]