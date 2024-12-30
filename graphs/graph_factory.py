from typing import Dict, Type
from graphs.conversational.graph import ConversationalGraph
from graphs.generic_graph import GenericGraph
from graphs.graph_params import GraphParams
from graphs.news.graph import NewsGraph

class GraphFactory:
    def __init__(self, graph_params: GraphParams, graph_mapping: Dict[str, Type[GenericGraph]] = None):
        self.graph_params = graph_params
        self.graph_mapping = {
            "Conversational AI": ConversationalGraph,
            "News AI": NewsGraph,
        }

    def create_graph(self) -> GenericGraph:
        graph_class = self.graph_mapping.get(self.graph_params.agent)
        if graph_class:
            return graph_class(self.graph_params)
        else:
            raise ValueError(f"Invalid graph name: {self.graph_params.agent}")