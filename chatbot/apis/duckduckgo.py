from typing import List
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from apis.dataclass.duckduckgo.news_results import NewsResult


search = DuckDuckGoSearchResults(backend="news", output_format="list", num_results=20)


class DuckDuckGo:
    async def search(query: str) -> List[NewsResult]:
        response = await search.ainvoke(query)
        return response
