import re
import asyncio
from pytubefix import YouTube
from pytubefix.cli import on_progress
import whisper

class PytubeTools:
    def __init__(self):
        self.loop = asyncio.get_event_loop()

    YOUTUBE_PATTERN = r'(https?:\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)[\w\-\_]+)'

    async def get_transcript(self, question: str) -> str:
        """get the transcript from a YouTube video"""
        model = whisper.load_model("medium")
        youtube_links = re.findall(self.YOUTUBE_PATTERN, question)
        transcript = ""
        for youtube_link in youtube_links:
            yt = YouTube(youtube_link, on_progress_callback=on_progress)
            if "a.en" in yt.captions:
                captions = yt.captions["a.en"]
            elif "a.fr" in yt.captions:
                captions = yt.captions["a.fr"]
            else:
                captions = None

            ## if there is a transcript use it, otherwise download the audio and transcribe it
            if captions:
                transcript = captions.generate_srt_captions()
            else:
                yt.streams.get_audio_only().download(output_path="./temp", filename="audio")
                result = await self.loop.run_in_executor(None, model.transcribe, "./temp/audio")
                transcript = result["text"]
        return transcript.strip()


