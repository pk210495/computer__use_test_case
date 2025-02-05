from langchain_openai import ChatOpenAI
from browser_use import Agent


import asyncio

llm = ChatOpenAI(model="gpt-4o",api_key="your_key")

async def main():
    agent = Agent(
        task="search all you can about the Explainable AI and write a 500 Word Essay on it",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
