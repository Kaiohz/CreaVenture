from langgraph.graph import StateGraph, START, END
from graphs.news.edges import NewsConditionalEdges
from graphs.news.state import NewsState
from graphs.news.nodes import NewsNodes
from graphs.generic_graph import GenericGraph
from langgraph.graph.state import CompiledStateGraph
from graphs.graph_params import GraphParams


class NewsGraph(GenericGraph):

    def __init__(self, graph_params: GraphParams):
        self.NewsGraph = StateGraph(NewsState)
        self.NewsNodes = NewsNodes(graph_params)
        self.NewsConditionalEdges = NewsConditionalEdges(graph_params)
        self.construct_graph()

    def construct_graph(self):
        ## nodes
        self.NewsGraph.add_node("country_finder", self.NewsNodes.find_country)
        self.NewsGraph.add_node("topic_finder", self.NewsNodes.find_topic)
        self.NewsGraph.add_node("generate", self.NewsNodes.generate)
        self.NewsGraph.add_node("fetch_news", self.NewsNodes.fetch_news)
        self.NewsGraph.add_node("start_node", self.NewsNodes.empty_node)
        ## edges
        self.NewsGraph.add_edge(START, "start_node")
        self.NewsGraph.add_conditional_edges(
            "start_node",
            self.NewsConditionalEdges.headlines_or_specific,
            {"Headlines": "country_finder", "Specific": "topic_finder"},
        )
        self.NewsGraph.add_edge("country_finder", "fetch_news")
        self.NewsGraph.add_edge("topic_finder", "fetch_news")
        self.NewsGraph.add_edge("fetch_news", "generate")
        self.NewsGraph.add_edge("generate", END)

    def get_graph(self) -> CompiledStateGraph:
        return self.NewsGraph.compile()
