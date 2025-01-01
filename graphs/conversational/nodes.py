from graphs.conversational.chains.generate import GenerateChain
from graphs.conversational.state import ConversationalState
from graphs.graph_params import GraphParams
from prompts.prompt_loader import PromptLoader

class ConversationalNodes():

    PromptLoader = PromptLoader()

    def __init__(self, graph_params: GraphParams):
        self.GenerateChain = GenerateChain(model=graph_params.model, temperature=graph_params.temperature, prompt=self.PromptLoader.load_prompt(graph_params.agent))

    async def generate(self, state) -> ConversationalState:
        question = state["question"]
        history = state["history"]
        print(f"question: {question}")
        print(f"history: {history}")
        generation = await self.GenerateChain.chain.ainvoke({"history": history, "question": question})
        return ConversationalState(question=question, history=history, final_answer=generation)