# Competitor Analysis Bot

To launch the development server:

Create a `.env` file with the required API keys.

```bash
cp .env.example .env
```

Then modify [.env](.env) with your OpenAI API key, Tavily API key, and optionally your LangSmith API key.

Next, install and start the server.

```bash
poetry install --with dev
poetry run langgraph up --port 8317
```

Please note that there've been some changes to LangGraph, in particular, to the use of Redis. I had to make sure to use the latest version of the langgraph-cli:
```bash
poetry add langgraph-cli@latest
```

Then start a run:

```python
from langgraph_sdk import get_client

client = get_client(url="http://localhost:8317")

# List all assistants
assistants = await client.assistants.search()

# We auto-create an assistant for each graph you register in config.
agent = assistants[0]
# Start a new thread
thread = await client.threads.create()

config = {"configurable": {"thread_id": "1"}, "max_concurrency": 3}

# Start a streaming run
input = {"base_product": "https://docs.smith.langchain.com/"}
async for chunk in client.runs.stream(
    thread["thread_id"], agent["assistant_id"], input=input
):
    print(chunk)
```

Please see the `research_script.py` file for a working example. When you have langgraph running, you can run:
```bash
poetry run python research_script.py
```
