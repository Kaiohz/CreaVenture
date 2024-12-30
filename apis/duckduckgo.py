from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

from apis.dataclass.duckduckgo.news_results import NewsResults

class DuckDuckGo:
    def __init__(self, backend: str):
        self.wrapper = DuckDuckGoSearchAPIWrapper()
        self.tool = DuckDuckGoSearchResults(api_wrapper=self.wrapper, backend=backend)

    async def search(self, query: str) -> NewsResults:
        response = NewsResults(**await self.tool.invoke(query))
        return response