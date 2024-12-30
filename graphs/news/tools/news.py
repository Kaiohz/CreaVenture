from typing import List, Tuple
from apis.dataclass.google.sources import SourcesResponse
from apis.dataclass.google.top_headlines import TopHeadlines
from apis.dataclass.google.articles import ArticlesResponse
from apis.google_news import GoogleNewsApi
from langgraph.prebuilt import ToolNode
from apis.duckduckgo import DuckDuckGo
from langchain_core.tools import tool


class NewsTools:
    DuckDuckGo = DuckDuckGo(backend="news")
    GoogleNewsApi = GoogleNewsApi()
    
    @tool
    async def get_top_headlines(country: str) -> Tuple[List[str], List[str]]:
        """Calls the Google News API to get the top headlines"""
        sources_response: SourcesResponse = await GoogleNewsApi.get_top_headlines_sources(country.lower())
        if len(sources_response.sources) == 0:
            return ["No sources found"]
        filtered_sources = [source for source in sources_response.sources if "google" not in source["id"]]
        sources_id = ",".join([source["id"] for source in filtered_sources[:3]])
        response: TopHeadlines = await GoogleNewsApi.get_top_headlines(sources_id)
        articles = response.articles
        descriptions: List[str] = [article["description"] for article in articles[:10]]
        sources: List[str] = [article["url"] for article in articles[:20]]
        response = await DuckDuckGo.search(f"latest news in {country}")
        descriptions.extend([result["snippet"] for result in response["results"]])
        sources.extend([result["link"] for result in response["results"]])
        return (descriptions, sources)
    
    @tool
    async def get_everything(question: str,topic: str) -> Tuple[List[str], List[str]]:
        """Calls the Google News API to get everything about a specific topic"""
        if topic == "" or topic is None:
            return ["No topic found"]
        articles_response: ArticlesResponse = await GoogleNewsApi.get_everything(topic)
        articles = articles_response.articles
        descriptions: List[str] = [article["description"] for article in articles[:10]]
        sources: List[str] = [article["url"] for article in articles[:20]]
        # Duplicated code, needs to find better way
        response = await DuckDuckGo.search(question)
        descriptions.extend([result["snippet"] for result in response["results"]])
        sources.extend([result["link"] for result in response["results"]])
        return (descriptions, sources)
    
    async def get_news_from_ddg(self, query: str) -> Tuple[List[str], List[str]]:
        """Calls the DuckDuckGo search API to get the news"""
        response = await self.DuckDuckGo.search(query)
        print(response)
        descriptions = [result["snippet"] for result in response["results"]]
        sources = [result["link"] for result in response["results"]]
        return (descriptions, sources)
    
    tools = [get_top_headlines, get_everything]
    tool_node = ToolNode(tools)


