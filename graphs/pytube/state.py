from typing import List

from typing_extensions import TypedDict


class PytubeState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        question: question asked by the user
        summaries: summaries of videos
        final_answer: final answer generated
    """

    question: str
    summaries: List[str]
    final_answer: str