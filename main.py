import chainlit as cl
from settings.chat_settings import ChatSettings
from profiles.chat_profiles import ChatProfiles
from core.essentials import CoreEssentials

chatSettings = ChatSettings().get_chat_settings()
chatProfiles = ChatProfiles().get_chat_profiles()
CoreEssentials = CoreEssentials()

@cl.set_chat_profiles
async def chat_profile():
    return chatProfiles

@cl.on_chat_start
async def on_chat_start():
    await CoreEssentials.setup_chat(chatSettings[0].values[0], chatSettings[1].initial)
    await cl.ChatSettings(chatSettings).send()

@cl.on_message
async def main(msg: cl.Message):
    response = await CoreEssentials.call_agent(msg)
    await CoreEssentials.process_response(response)

@cl.on_settings_update
async def setup_agent(settings):
    await CoreEssentials.setup_chat(settings["Model"], settings["Temperature"])
