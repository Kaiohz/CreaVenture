import asyncio  # added import
import os
import chainlit as cl
import chainlit.data as cld
from ollama import ResponseError, pull
from settings.chat_settings import ChatSettings
from profiles.chat_profiles import ChatProfiles
from core.essentials import CoreEssentials
from chainlit.data.sql_alchemy import SQLAlchemyDataLayer 

chatSettings = ChatSettings().get_chat_settings()
chatProfiles = ChatProfiles().get_chat_profiles()
CoreEssentials = CoreEssentials()

@cl.data_layer
def get_data_layer():
    return SQLAlchemyDataLayer(conninfo=os.environ.get("POSTGRE_CONNECTION_STRING"), storage_provider=None)

@cl.password_auth_callback
def auth_callback(username: str, password: str):
    if (username, password) == ("admin", "admin"):
        return cl.User(
            identifier="admin", metadata={"role": "admin", "provider": "credentials"}
        )
    else:
        return None

@cl.set_chat_profiles
async def chat_profile():
    return chatProfiles


@cl.on_chat_start
async def on_chat_start():
    await CoreEssentials.setup_chat(chatSettings[0].values[0], chatSettings[1].initial)
    await cl.ChatSettings(chatSettings).send()


@cl.on_message
async def main(msg: cl.Message):
    try:
        response = await CoreEssentials.call_agent(msg)
        await CoreEssentials.process_response(response)
    except ResponseError as e:
        model = cl.user_session.get("model")
        await cl.Message(content=f"Téléchargement du modèle {model}").send()
        await asyncio.get_running_loop().run_in_executor(None, pull, model.split("/")[1])
        await cl.Message(content=f"Téléchargement du modèle {model} terminé").send()
    except Exception as e:
        await cl.Message(content=f"{type(e).__name__}: {e}").send()


@cl.on_settings_update
async def setup_agent(settings):
    await CoreEssentials.setup_chat(settings["Model"], settings["Temperature"])