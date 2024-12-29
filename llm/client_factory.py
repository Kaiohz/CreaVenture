from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI

from llm.generic_client import LLMGenericClient

class LLMClientFactory:
    def __init__(self, model: str, temperature: float):
        self.model = model
        self.temperature = temperature
        self.model_mapping = {
            "Ollama": ChatOllama,
            "Google": ChatGoogleGenerativeAI,
        }

    def create_client(self) -> LLMGenericClient:
        category = self.model.split("/")[0]
        model = self.model.split("/")[1]
        client = self.model_mapping.get(category)(model=model, temperature=self.temperature)
        if not client:
            raise ValueError(f"Invalid model name: {self.model}")
        return client