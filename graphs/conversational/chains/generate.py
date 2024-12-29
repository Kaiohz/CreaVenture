from langchain_core.output_parsers import StrOutputParser
from llm.client_factory import LLMClientFactory 
from langchain.prompts import PromptTemplate

class GenerateChain():
    def __init__(self, model: str, temperature: float, prompt: str):
        prompt_template = PromptTemplate(template=prompt,input_variables=["history", "question"])
        llm = LLMClientFactory(model=model, temperature=temperature).create_client()
        self.chain = prompt_template | llm | StrOutputParser()