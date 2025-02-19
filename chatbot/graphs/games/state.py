from typing import List
from typing_extensions import TypedDict


class GamesFinderState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        question: question asked by the user
        history: history of messages
        final_answer: final answer generated
    """

    question: str
    report: str
    final_answer: str
