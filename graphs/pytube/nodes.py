import re
from graphs.pytube.chains.generate import GenerateChain
from graphs.pytube.chains.summarizer import SummarizerChain
from graphs.pytube.state import PytubeState
from graphs.graph_params import GraphParams
from graphs.pytube.tools.pytube import PytubeTools
from prompts.prompt_loader import PromptLoader

class PytubeNodes():

    PromptLoader = PromptLoader()

    def __init__(self, graph_params: GraphParams):
        self.SummarizerChain = SummarizerChain(model=graph_params.model, temperature=graph_params.temperature, prompt=self.PromptLoader.load_prompt("Summarizer"))
        self.GenerateChain = GenerateChain(model=graph_params.model, temperature=graph_params.temperature, prompt=self.PromptLoader.load_prompt(graph_params.agent))
        self.PytubeTools = PytubeTools()

    async def empty_node(self, state) -> PytubeState:
        """Empty node because i can't find how to add conditional edges to the start node"""
        question = state["question"]
        return PytubeState(question=question)
    
    async def summarizer(self, state) -> PytubeState:
        question = state["question"]
        summarization = ""
        if await self.PytubeTools.get_transcript(question):
            summarization = await self.SummarizerChain.chain.ainvoke({"transcript": question})
        return PytubeState(question=question, summarization=summarization)
    
    async def generate(self, state) -> PytubeState:
        question = state["question"]
        final_answer = await self.GenerateChain.chain.ainvoke({"question": question})
        return PytubeState(final_answer=final_answer)