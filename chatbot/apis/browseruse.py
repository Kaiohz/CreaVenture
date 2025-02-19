from apis.dataclass.browseruse.browser_use_request import BrowserUseRequest
from apis.dataclass.browseruse.browser_use_response import BrowserUseResponse
from apis.browser_use_client import BrowserUseClient
import asyncio
import concurrent.futures
import os


class BrowserUseApi:

    model_mapping = {
        "Mistral": ("mistral","pixtral-large-latest",os.environ.get("MISTRAL_API_KEY"), True),
        "Google": ("google","gemini-1.5-flash-latest",os.environ.get("GOOGLE_API_KEY"), True),
    }

    def __init__(self, model: str):
        self.api = BrowserUseClient()
        self.request_params = self.model_mapping.get(model.split("/")[0])

    async def run_task(self, task: str) -> BrowserUseResponse:
        """Execute a browser automation task"""
        request = BrowserUseRequest(task=task, llm_provider=self.request_params[0], llm_model_name=self.request_params[1], llm_api_key=self.request_params[2], use_vision=self.request_params[3])
        response = await self.api.predict(request)
        return response