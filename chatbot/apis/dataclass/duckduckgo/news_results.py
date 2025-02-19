from dataclasses import dataclass
@dataclass
class NewsResult:
    snippet: str
    title: str
    link: str
    date: str
    source: str
