from langchain_core.output_parsers import JsonOutputParser
from langchain.prompts import PromptTemplate
from llm.client_factory import LLMClientFactory


class HeadlinesOrSpecificChain:
    def __init__(self, model: str, temperature: float, prompt: str):
        prompt_template = PromptTemplate(template=prompt, input_variables=["question"])
        llm = LLMClientFactory(model=model, temperature=temperature).create_client()
        self.chain = prompt_template | llm | JsonOutputParser()
