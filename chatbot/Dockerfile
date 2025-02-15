FROM python:3.12.8-slim

WORKDIR /app

RUN apt-get update

RUN apt-get install build-essential -y

RUN pip install --upgrade pip

RUN pip install setuptools wheel

RUN pip install nvidia-pyindex

RUN pip install poetry

COPY pyproject.toml ./

RUN poetry install --no-root

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "chanlit", "run", "main.py", "--host", "0.0.0.0"]
