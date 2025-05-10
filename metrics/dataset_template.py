from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class EntryCategory(Enum):
    # easy facts (present in the text).
    FACTOID = 0
    # Definitions
    DEFINITION = 1
    # Answers that require some sort of a list as an response
    LIST = 2
    # Answers that require multiple steps or combination of information from many fragments
    CHAIN_OF_THOUGHT = 3
    # testing the ability to come up with logical conclusions
    INFERENCE = 4
    # questions that require longer answer
    OPEN_ENDED = 5
    # questions that require short straightforward answer + optional explanation
    CLOSE_ENDED = 6
    # questions that compare entities on various aspects
    COMPARATIVE = 7
    # summarization, simplification of a given text
    SUMMARIZATION = 8
    # inconsistencies or contradictions inside of a text
    # Company X has a net loss in 2023, ....... some text ....... Company X profited 500k in 2023.
    CONSISTENCY = 9
    # asking for an advice e.g. what should X do .....
    OPINION = 10
    # Questions that require creative thinking
    HYPOTHETICAL = 11

    DISTRACTION = 12


@dataclass
class DatasetEntry:
    question: str
    correct_answer: str
    relevant_contexts: list[str]
    category: EntryCategory
    file_path: str


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

    def __init__(self, data: list[DatasetEntry] | None = None):
        self.data = []

        if data:
            self.data.append(data)

    @abstractmethod
    def load_data(self, path: str) -> list[DatasetEntry]:
        pass
