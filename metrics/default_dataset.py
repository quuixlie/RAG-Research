from metrics.dataset_template import DatasetTemplate


class DefaultDataset(DatasetTemplate):
    data = [
        {
            "question": "What is the capital of France?",
            "correct_answer": "Paris",
            "relevant_contexts": [
                "The capital of France is Paris.",
                "Paris is known for its art, fashion, and culture."
            ],
            "file_path_relative_to_project_root": "TheLittlePrince.pdf"
        },
    ]