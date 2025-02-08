from abc import ABC, abstractmethod
from langgraph.graph.state import CompiledStateGraph


class GenericGraph(ABC):
    @abstractmethod
    def get_graph(self) -> CompiledStateGraph:
        pass
