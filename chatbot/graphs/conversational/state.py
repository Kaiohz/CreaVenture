from typing import List

from typing_extensions import TypedDict


class ConversationalState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        question: question asked by the user
        history: history of messages
        final_answer: final answer generated
    """

    question: str
    history: List[str]
    final_answer: str
