from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mistralai import ChatMistralAI
from llm.generic_client import LLMGenericClient
import os


class LLMClientFactory:
    def __init__(self, model: str, temperature: float):
        self.model = model
        self.temperature = temperature
        self.model_mapping = {
            "Ollama": ChatOllama,
            "Google": ChatGoogleGenerativeAI,
            "Mistral": ChatMistralAI,
        }

    def create_client(self) -> LLMGenericClient:
        category = self.model.split("/")[0]
        model = self.model.split("/")[1]        
        params = {"model": model, "temperature": self.temperature}
        if category == "Ollama":
            params["base_url"] = os.environ.get("OLLAMA_BASE_URL")
        client = self.model_mapping.get(category)(**params)
        if not client:
            raise ValueError(f"Invalid model name: {self.model}")
        return client
