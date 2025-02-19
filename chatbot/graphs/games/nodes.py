from apis.browseruse import BrowserUseApi
from graphs.games.chains.generate import GenerateChain
from graphs.games.state import GamesFinderState
from graphs.graph_params import GraphParams
from prompts.prompt_loader import PromptLoader



class GamesFinderNodes:

    PromptLoader = PromptLoader()

    def __init__(self, graph_params: GraphParams):
        self.GenerateChain = GenerateChain(
            model=graph_params.model,
            temperature=graph_params.temperature,
            prompt=self.PromptLoader.load_prompt(graph_params.agent),
        )
        self.BrowserUseApi = BrowserUseApi(model=graph_params.model)
        self.task=self.PromptLoader.load_prompt("GamesSearch")

    async def run_task(self, state) -> GamesFinderState:
        question = state["question"]
        task = f"{self.task} \n {question}".format(question=question)
        result = await self.BrowserUseApi.run_task(task)
        return GamesFinderState(
            question=state["question"], report=result
        )

    async def generate(self, state) -> GamesFinderState:
        question = state["question"]
        report = state["report"]
        generation = await self.GenerateChain.chain.ainvoke(
            {"report": report, "question": question}
        )
        return GamesFinderState(
            question=question, report=report, final_answer=generation
        )
