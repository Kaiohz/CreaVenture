from typing import List

from typing_extensions import TypedDict


class NewsState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        question: question asked by the user
        history: history of messages
        country: country to search
        sources: sources used to generate the answer
        summaries: summaries of articles
        final_answer: final answer generated
    """

    question: str
    topic: str
    country: str
    sources: List[str]
    headlines: List[str]
    final_answer: str