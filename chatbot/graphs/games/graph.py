from langgraph.graph import StateGraph, START, END
from graphs.games.state import GamesFinderState
from graphs.games.nodes import GamesFinderNodes
from graphs.generic_graph import GenericGraph
from langgraph.graph.state import CompiledStateGraph
from graphs.graph_params import GraphParams


class GamesFinderGraph(GenericGraph):

    def __init__(self, graph_params: GraphParams):
        self.BrowserUseGraph = StateGraph(GamesFinderState)
        self.BrowserUseNodes = GamesFinderNodes(graph_params)
        self.construct_graph()

    def construct_graph(self):
        self.BrowserUseGraph.add_node("run_task", self.BrowserUseNodes.run_task)
        self.BrowserUseGraph.add_node("generate", self.BrowserUseNodes.generate)
        self.BrowserUseGraph.add_edge(START, "run_task")
        self.BrowserUseGraph.add_edge("run_task", "generate")
        self.BrowserUseGraph.add_edge("generate", END)

    def get_graph(self) -> CompiledStateGraph:
        return self.BrowserUseGraph.compile()
