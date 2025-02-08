from typing import List
from chainlit.input_widget import Select, InputWidget, Slider


class ChatSettings:
    def get_chat_settings(self) -> List[InputWidget]:
        return [
            Select(
                id="Model",
                label="LLM Model",
                values=[
                    "Google/gemini-1.5-flash",
                    "Google/gemini-1.5-pro",
                    "Ollama/deepseek-r1",
                    "Ollama/llama3.2",
                    "Ollama/llama3.1",
                    "Ollama/qwen2.5",
                    "Ollama/mistral",
                ],
                initial_index=0,
            ),
            Slider(
                id="Temperature",
                label="Model Temperature",
                initial=0.0,
                min=0.0,
                max=1.0,
                step=0.1,
            ),
        ]
