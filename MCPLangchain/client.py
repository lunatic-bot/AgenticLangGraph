from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain.chat_models import init_chat_model

## load the environment
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

import asyncio

async def main():
    client = MultiServerMCPClient({
        "math":{
            "command": "python",
            "args": ["mathserver.py"], ## ensure correct absolute path
            "transport": "stdio",
        },
        "weather":{
            "url" : "http://localhost:8000/mcp", ## ensure correct url
            "transport": "streamable-http",
        }
    })


    tools = await client.get_tools()
    model = init_chat_model("groq:openai/gpt-oss-120b")

    agent = create_agent(
        model, tools
    )

    math_response = await agent.ainvoke({"messages" : [{"role" : "user", "content" : "What is 2 + 2?"}]})
    print("Math response : ",math_response['messages'][-1].content)


asyncio.run(main())
