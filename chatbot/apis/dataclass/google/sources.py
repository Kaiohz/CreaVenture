from dataclasses import dataclass
from typing import List


@dataclass
class Source:
    id: str
    name: str
    description: str
    url: str
    category: str
    language: str
    country: str


@dataclass
class SourcesResponse:
    status: str
    sources: List[Source]
