from apis.dataclass.browseruse.browser_use_request import BrowserUseRequest
from apis.dataclass.browseruse.browser_use_response import BrowserUseResponse
from gradio_client import Client
import asyncio
import os


class BrowserUseClient:
    client = Client(os.environ.get("BROWSER_USE_BASE_URL"))

    async def predict(self, request: BrowserUseRequest) -> BrowserUseResponse:
        response = await asyncio.to_thread(
            self.client.predict,
            agent_type=request.agent_type,
            llm_provider=request.llm_provider,
            llm_model_name=request.llm_model_name,
            llm_num_ctx=request.llm_num_ctx,
            llm_temperature=request.llm_temperature,
            llm_base_url=request.llm_base_url,
            llm_api_key=request.llm_api_key,
            use_own_browser=request.use_own_browser,
            keep_browser_open=request.keep_browser_open,
            headless=request.headless,
            disable_security=request.disable_security,
            window_w=request.window_w,
            window_h=request.window_h,
            save_recording_path=request.save_recording_path,
            save_agent_history_path=request.save_agent_history_path,
            save_trace_path=request.save_trace_path,
            enable_recording=request.enable_recording,
            task=request.task,
            add_infos=request.add_infos,
            max_steps=request.max_steps,
            use_vision=request.use_vision,
            max_actions_per_step=request.max_actions_per_step,
            tool_calling_method=request.tool_calling_method,
            api_name="/run_with_stream",
        )
        return BrowserUseResponse(markdown_content=response[1], file_path=None)
