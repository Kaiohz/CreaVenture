from dataclasses import dataclass
from datetime import datetime

@dataclass
class NewsResult:
    snippet: str
    title: str
    link: str
    date: str
    source: str