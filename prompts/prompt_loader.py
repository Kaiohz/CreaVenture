import os 
class PromptLoader:
     prompt_mapping = {
        "Freelancer AI" : "freelancer/generate",
        ## Conversational agent
        "Conversational AI" : "conversational/generate",
        ## News agent
        "News AI" : "news/generate",
        "CountryFinder": "news/country_finder",
        "TopicFinder": "news/topic_finder",
        "HeadlinesOrSpecific": "news/headlines_or_specific",
        "FetchNews": "news/fetch_news",
        ## Pytube agent
        "Pytube AI" : "pytube/generate",
        "Summarizer": "pytube/summarizer",
        "IsYoutubeLink": "pytube/is_youtube_link",
    }

     def load_prompt(self,chat_profile: str) -> str:
        prompt_path = os.path.join(os.path.dirname(__file__), "graphs", f"{self.prompt_mapping.get(chat_profile)}.txt")
        try:
            with open(prompt_path, "r", encoding="utf-8") as f:
                return f.read().strip()
        except FileNotFoundError:
            return "You are a helpful AI assistant."