import asyncio
import os
import chainlit as cl
from ollama import ResponseError, pull
from settings.chat_settings import ChatSettings
from profiles.chat_profiles import ChatProfiles
from core.essentials import CoreEssentials
from chainlit.data.sql_alchemy import SQLAlchemyDataLayer
from chainlit.types import ThreadDict

chatSettings = ChatSettings().get_chat_settings()
chatProfiles = ChatProfiles().get_chat_profiles()
CoreEssentials = CoreEssentials()


@cl.data_layer
def get_data_layer():
    return SQLAlchemyDataLayer(
        conninfo=os.environ.get("POSTGRE_CONNECTION_STRING"), storage_provider=None
    )


@cl.on_chat_resume
async def resume_conversation(thread: ThreadDict):
    settings = thread.get("metadata").get("chat_settings")
    await CoreEssentials.setup_chat(settings["Model"], settings["Temperature"])
    await cl.ChatSettings(chatSettings).send()


@cl.password_auth_callback
def auth_callback(username: str, password: str):
    if username == "admin" and password == "admin":
        return cl.User(
            identifier="admin", metadata={"role": "admin", "provider": "credentials"}
        )
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
        loading_msg = cl.Message(content=f"Téléchargement du modèle {model}")
        await loading_msg.send()

        await loading_msg.update(
            content=f"Téléchargement du modèle {model} en cours.", streaming=True
        )
        for _ in range(3):
            for dots in [".", "..", "..."]:
                await loading_msg.update(
                    content=f"Téléchargement du modèle {model} en cours{dots}",
                    streaming=True,
                )
                await asyncio.sleep(0.5)

        await asyncio.get_running_loop().run_in_executor(
            None, pull, model.split("/")[1]
        )
        await loading_msg.update(content=f"Téléchargement du modèle {model} terminé")
    except Exception as e:
        await cl.Message(content=f"{type(e).__name__}: {e}").send()


@cl.on_settings_update
async def setup_agent(settings):
    await CoreEssentials.setup_chat(settings["Model"], settings["Temperature"])
