from typing import List
import chainlit as cl

profiles = [
    cl.ChatProfile(
        name="Conversational AI",
        markdown_description="To have a conversation with the selected model. You can change the model from the **settings**.",
        icon="public/avatars/my_assistant.png",
    ),
    cl.ChatProfile(
        name="News AI",
        markdown_description="Help you to stay updated on what's happening in the world. You can change the model from the **settings**.",
        icon="public/avatars/news.png",
        hasSources=True,
    ),
]

class ChatProfiles:
     def get_chat_profiles(self) -> List[cl.ChatProfile]:
        return profiles