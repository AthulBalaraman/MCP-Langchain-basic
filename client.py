from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    # Initialize the Groq client with your API key
    print("Initializing MultiServerMCPClient...")
    client = MultiServerMCPClient(
        {
            "math-server" : {
            "command": "python",
            "args": ["math-server.py"], #Ensure correct abslute path 
            "transport":"stdio"
            },
            "weather-server" : {
                "url": "http://localhost:8000",
                "transport": "streamable-http"
            }
        }
        )
    
    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY") 
    # Replace with your actual API key
    print("GROQ_API_KEY set successfully.", os.getenv("GROQ_API_KEY") is not None)
    print("Fetching tools from the servers...")
    tools = await client.get_tools()
    print("Tools fetched successfully:", tools)
    model = ChatGroq(model = "qwen-qwaq-32b")
    agent = create_react_agent(
        model, tools 
    )
    print("Agent created successfully.")
    
    math_response = await agent.ainvoke({"message":[{"role": "user", "content": "What is (3 + 5) *2?"}]})
    print("Math Response:", math_response['message'][-1].content )
    weather_response = await agent.ainvoke({"message":[{"role": "user", "content": "What is the weather in california today?"}]})
    print("Weather Response:", weather_response['message'][-1].content)


asyncio.run(main())