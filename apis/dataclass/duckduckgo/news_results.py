from dataclasses import dataclass
from typing import List

@dataclass
class NewsResult:
    snippet: str
    title: str
    link: str

@dataclass
class NewsResults:
    results: List[NewsResult]
