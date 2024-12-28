from graphs.generic_graph import GenericGraph
from graphs.graph_params import GraphParams
from constants.graph_mapping import graph_mapping

class GraphFactory:
    def __init__(self, graph_params: GraphParams):
        self.graph_params = graph_params

    def create_graph(self) -> GenericGraph:
        if graph_mapping.get(self.graph_params.agent):
            return graph_mapping[self.graph_params.agent](self.graph_params)
        else:
            raise ValueError('Invalid graph name')