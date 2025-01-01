from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from llm.client_factory import LLMClientFactory

class ConversationChain():
    def __init__(self, model: str, temperature: float, prompt: str):
        prompt_template = PromptTemplate(template=prompt,input_variables=["question","history"])
        llm = LLMClientFactory(model=model, temperature=temperature).create_client()
        self.chain = prompt_template | llm | StrOutputParser()