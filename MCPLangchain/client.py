from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_react_agent
from langchain_groq import ChatGroq

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
