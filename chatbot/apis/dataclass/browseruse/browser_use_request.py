from dataclasses import dataclass

@dataclass
class BrowserUseRequest:
    llm_provider: str
    llm_model_name: str
    llm_api_key: str
    task: str
    use_vision: bool

    agent_type: str = "custom"
    llm_num_ctx: int = 32000
    llm_temperature: float = 1.0
    llm_base_url: str = ""
    use_own_browser: bool = False
    keep_browser_open: bool = False
    headless: bool = False
    disable_security: bool = True
    window_w: int = 1280
    window_h: int = 1100
    save_recording_path: str = "./tmp/record_videos"
    save_agent_history_path: str = "./tmp/agent_history"
    save_trace_path: str = "./tmp/traces"
    enable_recording: bool = True
    add_infos: str = ""
    max_steps: int = 100
    max_actions_per_step: int = 10
    tool_calling_method: str = "auto"

    def to_gradio_data(self) -> dict:
        """Convert request to Gradio API format"""
        return {
            "data": [
                self.task,
                self.llm_provider,
                self.llm_model_name, 
                self.llm_api_key,
                self.use_vision,
                self.save_recording_path,
                self.save_agent_history_path,
                self.use_own_browser,
                self.keep_browser_open,
                self.headless,
                self.disable_security,
                self.window_w,
                self.window_h,
                self.save_recording_path,
                self.save_agent_history_path,
                self.save_trace_path,
                self.enable_recording,
                self.add_infos,
                "",
                self.max_steps,
                True,
                self.max_actions_per_step,
                self.tool_calling_method
            ]
        }