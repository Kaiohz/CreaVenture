import os 
from constants.prompt_mapping import prompt_mapping
class PromptLoader:
     def load_prompt(self,chat_profile: str) -> str:
        prompt_path = os.path.join(os.path.dirname(__file__), "graphs", f"{prompt_mapping.get(chat_profile)}.txt")
        try:
            with open(prompt_path, "r", encoding="utf-8") as f:
                return f.read().strip()
        except FileNotFoundError:
            return "You are a helpful AI assistant."