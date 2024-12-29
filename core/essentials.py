from typing import Any, AsyncIterator
import chainlit as cl
from graphs.generic_graph import GenericGraph
from langchain_core.messages import AIMessageChunk
from graphs.graph_factory import GraphFactory
from graphs.graph_params import GraphParams

class CoreEssentials:

    nodes_mapping = {
        "Conversational AI": "",
        "News AI": "fetch_news",
        "Pytube AI": ""
    }

    def __init__(self):
        self.graph_params = GraphParams()
        self.graph_factory = GraphFactory(self.graph_params)

    async def setup_chat(self,model: str, temperature: float):
        chat_profile: str= cl.user_session.get("chat_profile")
        self.graph_params.agent = chat_profile
        self.graph_params.model = model
        self.graph_params.temperature = temperature
        graph = self.graph_factory.create_graph()
        cl.user_session.set("model", model)
        cl.user_session.set("temperature", temperature)
        cl.user_session.set("graph", graph)

    async def call_agent(self,msg: cl.Message) -> AsyncIterator[dict[str, Any] | Any]:
        graph: GenericGraph = cl.user_session.get("graph")
        chat_history = cl.chat_context.to_openai()[-4:-1]
        response = graph.get_graph().astream({"question": msg.content, "history": chat_history}, stream_mode=["messages","updates"])
        return response

    async def process_response(self,response: AsyncIterator[dict[str, Any] | Any]):
        answer = cl.Message(content="")
        async for chunk in response:
            if chunk[0] == "messages" and chunk[1][1]["langgraph_node"] == "generate":
                values: AIMessageChunk = chunk[1][0]
                await answer.stream_token(values.content)
            node_name = self.nodes_mapping[cl.user_session.get("chat_profile")]
            if node_name:
                await self.process_sources(node_name,chunk,answer)
        await answer.send()

    async def process_sources(self, node_name: str,chunk,answer: cl.Message) -> cl.Message:
        if chunk[0] == "updates":
            if node_name in chunk[1] and "sources" in chunk[1][node_name]:
                sources = chunk[1][node_name]["sources"]
                formatted_sources = "\n".join(sources)
                settings = f"{cl.user_session.get('chat_profile')} - Model : {cl.user_session.get('model')} - Temperature : {cl.user_session.get('temperature')}\n"
                sources = f"Sources:\n{formatted_sources}"
                answer.elements.append(cl.Text(content=f"{settings}{sources}", display="inline"))
        return answer
