from langgraph_sdk import get_client
import asyncio

async def main():
    client = get_client(url="http://localhost:8317")
    # List all assistants
    assistants = await client.assistants.search()
    # We auto-create an assistant for each graph you register in config.
    agent = assistants[0]
    # Start a new thread
    thread = await client.threads.create()
    
    config = {
        "configurable": {
            "thread_id": "1"
        }, 
        "max_concurrency": 3
    }
    
    # Start a streaming run
    input = {"base_product": "https://docs.smith.langchain.com/"}
    async for chunk in client.runs.stream(
        thread["thread_id"], agent["assistant_id"], input=input
    ):
        print(chunk)
    
    return agent, thread

if __name__ == "__main__":
    asyncio.run(main())
