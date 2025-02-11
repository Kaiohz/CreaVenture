from typing import List, Tuple
from apis.dataclass.google.sources import SourcesResponse
from apis.dataclass.google.top_headlines import TopHeadlines
from apis.dataclass.google.articles import ArticlesResponse
from apis.google_news import GoogleNewsApi
from langgraph.prebuilt import ToolNode
from apis.duckduckgo import DuckDuckGo
from langchain_core.tools import tool
from crawl4ai import AsyncWebCrawler


class NewsTools:

    @tool
    async def get_top_headlines(
        question: str, country_code: str
    ) -> Tuple[List[str], List[str]]:
        """Calls the Google News API to get the top headlines when there is no specific topic there is two parameters country_code and question"""
        sources = []
        descriptions = []
        try:
            sources_response = []
            if country_code:
                sources_response: SourcesResponse = (
                    await GoogleNewsApi.get_top_headlines_sources(country_code.lower())
                )
            if len(sources_response.sources) > 0:
                filtered_sources = [
                    source
                    for source in sources_response.sources
                    if "google" not in source["id"]
                ]
                sources_id = ",".join([source["id"] for source in filtered_sources])
                response: TopHeadlines = await GoogleNewsApi.get_top_headlines(
                    sources_id
                )
                articles = response.articles
                descriptions: List[str] = [
                    article["description"] for article in articles[:10]
                ]
                sources: List[str] = [article["url"] for article in articles[:10]]
        except:
            descriptions: List[str] = []
            sources: List[str] = []

        try:
            duck_duck_response = await DuckDuckGo.search(question)
            duck_duck_descriptions = [
                result["snippet"] for result in duck_duck_response
            ]
            duck_duck_sources = [result["link"] for result in duck_duck_response]
            descriptions.extend(duck_duck_descriptions)
            sources.extend(duck_duck_sources)
        except:
            descriptions: List[str] = []
            sources: List[str] = []

        return (descriptions, sources)

    @tool
    async def get_everything(question: str, topic: str) -> Tuple[List[str], List[str]]:
        """Calls the Google News API to get everything about a specific topic there is two parameters topic and question"""
        sources = []
        descriptions = []
        try:
            if topic:
                articles_response: ArticlesResponse = (
                    await GoogleNewsApi.get_everything(topic)
                )
                articles = articles_response.articles
                descriptions: List[str] = [
                    article["description"] for article in articles[:10]
                ]
                sources: List[str] = [article["url"] for article in articles[:10]]
        except:
            descriptions: List[str] = []
            sources: List[str] = []

        try:
            duck_duck_response = await DuckDuckGo.search(question)
            duck_duck_descriptions = [
                result["snippet"] for result in duck_duck_response
            ]
            duck_duck_sources = [result["link"] for result in duck_duck_response]
            descriptions.extend(duck_duck_descriptions)
            sources.extend(duck_duck_sources)
        except:
            descriptions: List[str] = []
            sources: List[str] = []

        return (descriptions, sources)
    
    @tool
    async def crawl_article(source: str) -> str:
        """Crawls the article from the source, there is one parameter source"""
        async with AsyncWebCrawler() as crawler:
            article = await crawler.arun(url=source)
            return article

    tools = [get_top_headlines, get_everything, crawl_article]
    tool_node = ToolNode(tools)
