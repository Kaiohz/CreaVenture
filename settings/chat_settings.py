from typing import List
from chainlit.input_widget import Select, Switch, InputWidget, Slider

class ChatSettings:
     def get_chat_settings(self) -> List[InputWidget]:
        return [
            Select(
                id="Model",
                label="LLM Model",
                values=["Ollama/llama3.2", "Ollama/llama3.1","Ollama/qwen2.5", "Ollama/mistral","Google/gemini-1.5-flash","Google/gemini-1.5-pro","Google/gemini-1.5.flash-8b"],
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