from typing import List
from graphs.news.chains.headlines_or_specific import HeadlinesOrSpecificChain
from graphs.news.models.choice import ChoiceModel
from graphs.graph_params import GraphParams
from prompts.prompt_loader import PromptLoader


class NewsConditionalEdges():
    PromptLoader = PromptLoader()

    def __init__(self, graph_params: GraphParams):
        self.HeadlinesOrSpecificChain = HeadlinesOrSpecificChain(model=graph_params.model, temperature=graph_params.temperature, prompt=self.PromptLoader.load_prompt("HeadlinesOrSpecific"))

    async def headlines_or_specific(self, state) -> str:
        question = state["question"]
        choice_model: ChoiceModel = ChoiceModel(**await self.HeadlinesOrSpecificChain.chain.ainvoke({"question": question}))
        print(choice_model.choice)
        return choice_model.choice