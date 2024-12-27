# Chainlit LLM Application 🚀🤖

A Python application built with Chainlit for interacting with Large Language Models.

## Project Structure
```
.  
├── apis/         # API integrations including Google News  
├── graphs/       # Graph implementations for conversation flows  
├── profiles/     # Chat profile configurations  
├── prompts/      # LLM prompt templates and loader  
├── public/       # Static assets and avatars  
├── settings/     # Application settings and configurations  
└── main.py       # Entry point of the application
```

## Getting Started

### Install Dependencies
```bash
pip install -r requirements.txt
ollama pull llama3.2 llama3.1 qwen2.5 mistral
cp .env.example .env
```

### Configure Environment
- Copy `.env.example` to `.env`
- Update the environment variables as needed

### Run the Application
```bash
chainlit run main.py -w
```

- Access the application at [http://localhost:8000](http://localhost:8000)

## Features
- **API integrations** with Google News
- **Graph implementations** for conversation flows
- **Chat profile configurations**
- **LLM prompt templates and loader**
- **Application settings and configurations**

## Extras
- **Langgraph Tutorials**: [Langgraph Tutorials on GitHub](https://github.com/langchain-ai/langgraph/tree/main/docs/docs/tutorials)

## Useful Links
- **Documentation**: Get started with our comprehensive Chainlit Documentation at [https://docs.chainlit.io](https://docs.chainlit.io)
