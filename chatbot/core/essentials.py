from typing import Any, AsyncIterator
import chainlit as cl
from graphs.generic_graph import GenericGraph
from langchain_core.messages import AIMessageChunk
from graphs.graph_factory import GraphFactory
from graphs.graph_params import GraphParams
from langchain.schema.runnable.config import RunnableConfig


class CoreEssentials:

    nodes_mapping = {
        "Conversational AI": "generate",
        "News AI": "generate,fetch_news",
        "Pytube AI": "generate",
        "Games Finder AI": "generate",
    }

    def __init__(self):
        self.graph_params = GraphParams()
        self.graph_factory = GraphFactory(self.graph_params)

    async def setup_chat(self, model: str, temperature: float):
        # Copilot
        self.graph_params.agent = (
            cl.user_session.get("chat_profile") or "Conversational AI"
        )
        self.graph_params.model = model
        self.graph_params.temperature = temperature
        cl.user_session.set("model", model)
        cl.user_session.set("temperature", temperature)
        cl.user_session.set("graph", self.graph_factory.create_graph())

    async def call_agent(self, msg: cl.Message) -> AsyncIterator[dict[str, Any] | Any]:
        graph: GenericGraph = cl.user_session.get("graph")
        chat_history = cl.chat_context.to_openai()[-4:-1]
        config = {"configurable": {"thread_id": cl.context.session.id}}
        cb = cl.LangchainCallbackHandler()
        response = graph.get_graph().astream(
            {"question": msg.content, "history": chat_history},
            stream_mode=["messages", "updates"],
            config=RunnableConfig(callbacks=[cb], **config),
        )
        return response

    async def process_response(self, response: AsyncIterator[dict[str, Any] | Any]):
        answer = cl.Message(content="")
        # Copilot
        node = cl.user_session.get("chat_profile") or "Conversational AI"
        node_name = self.nodes_mapping[node]
        final_node = node_name.split(",")[0]
        sources_node = (
            node_name.split(",")[1] if len(node_name.split(",")) > 1 else None
        )
        settings = f"{cl.user_session.get('chat_profile')} - Model : {cl.user_session.get('model')} - Temperature : {cl.user_session.get('temperature')}\n"
        answer.elements.append(cl.Text(content=f"{settings}", display="inline"))
        async for chunk in response:
            if chunk[0] == "messages" and chunk[1][1]["langgraph_node"] == final_node:
                values: AIMessageChunk = chunk[1][0]
                await answer.stream_token(values.content)
            if node_name:
                await self.process_sources(sources_node, chunk, answer)
        await answer.send()

    async def process_sources(self, node_name: str, chunk, answer: cl.Message) -> str:
        sources = []
        if chunk[0] == "updates":
            if node_name in chunk[1] and "sources" in chunk[1][node_name]:
                sources = chunk[1][node_name]["sources"]
                formatted_sources = "\n".join(sources)
                sources = f"Sources:\n{formatted_sources}"
                answer.elements.append(cl.Text(content=f"{sources}", display="inline"))
        return sources
