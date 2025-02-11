from langchain_core.output_parsers import JsonOutputParser
from langchain.prompts import PromptTemplate
from graphs.news.tools.news import NewsTools
from llm.client_factory import LLMClientFactory


class ArticleCrawlerChain:
    def __init__(self, model: str, temperature: float, prompt: str):
        prompt_template = PromptTemplate(template=prompt, input_variables=["source"])
        tools = NewsTools().tools
        llm = LLMClientFactory(model=model, temperature=temperature).create_client()
        self.chain_with_tools = prompt_template | llm.bind_tools(tools)
        self.tool_node = NewsTools().tool_node