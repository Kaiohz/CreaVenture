import re
from pytube import YouTube
import whisper

class PytubeTools:
    def __init__(self):
        self.model = whisper.load_model("turbo")

    YOUTUBE_PATTERN = r'http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?'

    async def get_transcript(self, question: str) -> str:
        """get the transcript from a YouTube video"""
        youtube_link = None
        match = re.search(self.YOUTUBE_PATTERN, question)
        if match:
            youtube_link = match.group(0)
        if youtube_link:
            YouTube(youtube_link).streams.filter(only_audio=True).first().download("./temp/audio.mp3")
            result = self.model.transcribe("./temp/audio.mp3")
            return result["text"]
        return ""    


