class GraphParams:
    def __init__(
        self,
        agent: str = None,
        model: str = None,
        temperature: float = None,
        embeddings: str = None,
    ):
        self.agent = agent
        self.model = model
        self.temperature = temperature
        self.embeddings = embeddings
