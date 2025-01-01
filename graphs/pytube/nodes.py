import re
from graphs.pytube.chains.conversation import ConversationChain
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
        return PytubeState(question=state["question"])
    
    async def summarizer(self, state) -> PytubeState:
        question = state["question"]
        transcript = await self.PytubeTools.get_transcript(question)
        if transcript:
            summaries = await self.SummarizerChain.chain.ainvoke({"transcript": transcript})
        return PytubeState(summaries=summaries)
    
    async def generate(self, state) -> PytubeState:
        question = state["question"]
        summaries = state["summaries"] if "summaries" in state else []
        final_answer = await self.GenerateChain.chain.ainvoke({"question": question,"summaries": summaries})
        return PytubeState(final_answer=final_answer, summaries=[])