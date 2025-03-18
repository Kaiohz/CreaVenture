import re
from prompts.prompt_loader import PromptLoader


class PytubeConditionalEdges:
    PromptLoader = PromptLoader()
    YOUTUBE_PATTERN = (
        r"(https?:\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)[\w\-\_]+)"
    )

    async def is_youtube_link(self, state) -> str:
        question = state["question"]
        match = re.search(self.YOUTUBE_PATTERN, question)
        return "yes" if match else "no"
