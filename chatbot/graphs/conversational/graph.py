from langgraph.graph import StateGraph, START, END
from graphs.conversational.state import ConversationalState
from graphs.conversational.nodes import ConversationalNodes
from graphs.generic_graph import GenericGraph
from langgraph.graph.state import CompiledStateGraph
from graphs.graph_params import GraphParams


class ConversationalGraph(GenericGraph):

    def __init__(self, graph_params: GraphParams):
        self.ConversationalGraph = StateGraph(ConversationalState)
        self.ConversationalNodes = ConversationalNodes(graph_params)
        self.construct_graph()

    def construct_graph(self):
        self.ConversationalGraph.add_node("generate", self.ConversationalNodes.generate)
        self.ConversationalGraph.add_edge(START, "generate")
        self.ConversationalGraph.add_edge("generate", END)

    def get_graph(self) -> CompiledStateGraph:
        return self.ConversationalGraph.compile()
