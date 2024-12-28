from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Source:
    id: Optional[str]
    name: str

@dataclass
class Article:
    source: Source
    author: str
    title: str
    description: str
    url: str
    urlToImage: str
    publishedAt: str
    content: str

@dataclass
class TopHeadlines:
    status: str
    totalResults: int
    articles: List[Article]
