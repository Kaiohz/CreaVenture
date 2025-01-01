import re
from graphs.graph_params import GraphParams
from graphs.pytube.chains.is_youtube_link import IsYoutubeLinkChain
from graphs.pytube.models.binary import BinaryModel
from prompts.prompt_loader import PromptLoader

class PytubeConditionalEdges():
    PromptLoader = PromptLoader()
    youtube_pattern = r'http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?'
    
    async def is_youtube_link(self, state) -> str:
        question = state["question"]
        match = re.search(self.youtube_pattern, question)
        return "yes" if match else "no"