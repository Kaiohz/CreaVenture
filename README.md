# Chainlit LLM Application 🚀🤖

A Python application built with Chainlit for interacting with Large Language Models.

## Project Structure
```
.  
├── apis/         # API integrations including Google News  
├── graphs/       # Graph implementations for conversation flows
├── core/         # Core methods
├── llm/          # LLm clients
├── profiles/     # Chat profile configurations  
├── prompts/      # LLM prompt templates and loader  
├── public/       # Static assets and avatars  
├── settings/     # Application settings and configurations  
├── main.py       # Entry point of the application
└── README.md     # Project documentation
```

## Getting Started

### Install Dependencies
```bash
git clone --recurse-submodules https://github.com/Kaiohz/CreaVenture.git
cd chatbot 
curl https://pyenv.run | bash
pyenv install 3.12
pyenv global 3.12
poetry install
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.2 
ollama pull llama3.1
ollama pull qwen2.5
ollama pull mistral
playwright install
cp .env.example .env
```

## Get GoogleNews API key

https://newsapi.org/s/google-news-fr-api

## Get your Gemini key if you want to gemini-1.5-flash

https://aistudio.google.com/

## Get your Mistral API key 

https://auth.mistral.ai/ui/login

### Configure Environment
- Copy for chatbot `.env.example` to `.env`
- Update the environment variables as needed

### Docker
- Copy for chatbot `.env.example` to `.env.docker`
- change hostnames to match services in docker-compose.yml
```bash
docker-compose up
```

### Run the Chatbot
```bash
poetry run chainlit run chainlit.py -w
```

- Access the application at [http://localhost:8000](http://localhost:8000)
- Default login/password admin/admin

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
