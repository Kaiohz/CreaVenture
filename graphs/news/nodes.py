import json
from typing import List
from graphs.news.chains.fetch_news import FetchNewsChain
from graphs.news.chains.generate import GenerateChain
from graphs.news.chains.country_finder import CountryFinderChain
from graphs.news.chains.headlines_or_specific import HeadlinesOrSpecificChain
from graphs.news.chains.topic_finder import TopicFinderChain
from graphs.news.models.choice import ChoiceModel
from graphs.news.models.country import CountryModel
from graphs.news.models.topic import TopicModel
from graphs.news.state import NewsState
from graphs.graph_params import GraphParams
from prompts.prompt_loader import PromptLoader


class NewsNodes():
    PromptLoader = PromptLoader()

    def __init__(self, graph_params: GraphParams):
        self.CountryFinderChain = CountryFinderChain(model=graph_params.model, temperature=graph_params.temperature, prompt=self.PromptLoader.load_prompt("CountryFinder"))
        self.TopicFinderChain = TopicFinderChain(model=graph_params.model, temperature=graph_params.temperature, prompt=self.PromptLoader.load_prompt("TopicFinder"))
        self.FetchNewsChain = FetchNewsChain(model=graph_params.model, temperature=graph_params.temperature, prompt=self.PromptLoader.load_prompt("FetchNews"))
        self.GenerateChain = GenerateChain(model=graph_params.model, temperature=graph_params.temperature, prompt=self.PromptLoader.load_prompt(graph_params.agent))

    
    async def empty_node(self, state) -> NewsState:
        """Empty node because i can't find how to add conditional edges to the start node"""
        question = state["question"]
        return NewsState(question=question)
    
    async def find_country(self, state) -> NewsState:
        question = state["question"]
        country = CountryModel(**await self.CountryFinderChain.chain.ainvoke({"question": question}))
        return NewsState(question=question, country=country.code)
    
    async def find_topic(self, state) -> NewsState:
        question = state["question"]
        topic = TopicModel(**await self.TopicFinderChain.chain.ainvoke({"question": question}))
        return NewsState(question=question, topic=topic)
    
    async def fetch_news(self, state) -> NewsState:
        question = state["question"]
        country = state["country"] if "country" in state else ""
        response = await self.FetchNewsChain.tool_node.ainvoke({"messages": [await self.FetchNewsChain.chain_with_tools.ainvoke({"question": question, "country": country})]})
        content: List[str] = response["messages"][0].content
        headlines_sources = tuple(json.loads(content))
        headlines = headlines_sources[0] if len(headlines_sources[0]) and headlines_sources[0] else []
        sources = headlines_sources[1] if len(headlines_sources) > 1 and headlines_sources[1] else []
        return NewsState(question=question, headlines=headlines, sources=sources)
    
    async def generate(self, state) -> NewsState:
        headlines = state["headlines"]
        generation = await self.GenerateChain.chain.ainvoke({"headlines": headlines})
        return NewsState(final_answer=generation)