from typing import List
from apis.dataclass.google.articles import ArticlesResponse
from apis.generic import GenericApi
from config import GoogleNewsConfig
from apis.dataclass.google.top_headlines import TopHeadlines
from apis.dataclass.google.sources import SourcesResponse
from datetime import datetime, timedelta

## Config
Api = GenericApi()
GoogleNewsConfig = GoogleNewsConfig()
Api.base_url = GoogleNewsConfig.BASE_URL
Api.headers = {"Content-Type": "application/json"}
Api.timeout = 10
api_key = GoogleNewsConfig.API_KEY
## Endpoints
headlines_sources_endpoint = "/v2/top-headlines/sources"
top_headlines_endpoint = "/v2/top-headlines"
everything_endpoint = "/v2/everything"

class GoogleNewsApi():
    async def get_top_headlines_sources(country: str) -> SourcesResponse:
        params = {"apiKey": api_key, "country": country}
        sources_response: SourcesResponse = SourcesResponse(**await Api.get(headlines_sources_endpoint, params=params))
        return sources_response

    async def get_top_headlines(sources: List[str]) -> TopHeadlines:
        params = {"apiKey": api_key, "sources": sources}
        top_headlines_response = TopHeadlines(**await Api.get(top_headlines_endpoint, params=params))
        return top_headlines_response
    
    async def get_everything(topic: str) -> ArticlesResponse:
        from_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        params = {"apiKey": api_key, "q": topic, "sortBy": "relevancy", "searchIn": "title,description","from": from_date}
        articles_response: ArticlesResponse = ArticlesResponse(**await Api.get(everything_endpoint, params=params))
        return articles_response
