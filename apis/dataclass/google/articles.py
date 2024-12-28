from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Source:
    id: Optional[str]
    name: str

@dataclass
class Article:
    source: Source
    author: Optional[str]
    title: str
    description: Optional[str]
    url: str
    urlToImage: Optional[str]
    publishedAt: str
    content: Optional[str]

@dataclass
class ArticlesResponse:
    status: str
    totalResults: int
    articles: List[Article]
