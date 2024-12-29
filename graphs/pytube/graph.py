from langgraph.graph import StateGraph, START, END
from graphs.pytube.edges import PytubeConditionalEdges
from graphs.pytube.state import PytubeState
from graphs.pytube.nodes import PytubeNodes
from graphs.generic_graph import GenericGraph
from langgraph.graph.state import CompiledStateGraph
from graphs.graph_params import GraphParams

class PytubeGraph(GenericGraph):

    def __init__(self, graph_params: GraphParams):
        self.PytubeGraph = StateGraph(PytubeState)
        self.PytubeNodes = PytubeNodes(graph_params)
        self.PytubeEdges = PytubeConditionalEdges()
        self.construct_graph()

    def construct_graph(self):
        self.PytubeGraph.add_node("empty_node", self.PytubeNodes.empty_node)
        self.PytubeGraph.add_node("summarizer", self.PytubeNodes.summarizer)
        self.PytubeGraph.add_node("generate", self.PytubeNodes.generate)

        self.PytubeGraph.add_edge(START, "empty_node")

        self.PytubeGraph.add_conditional_edges(
            "empty_node",
            self.PytubeEdges.is_youtube_link,
            {
                "yes": "summarizer",
                "no": "generate"
            }
        )
        
        self.PytubeGraph.add_edge("summarizer", "generate")
        self.PytubeGraph.add_edge("generate", END)

    def get_graph(self) -> CompiledStateGraph:
        return self.PytubeGraph.compile()
