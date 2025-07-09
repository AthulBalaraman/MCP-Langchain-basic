from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather-Server")

@mcp.tool("get_weather")
async def get_weather(location: str) -> str:
    """Fetches the current weather for a given city."""
    print(f"Fetching weather for {location}...")
    # In a real application, you would call a weather API here.
    # For demonstration purposes, we'll return a mock response.
    return f"The current weather in {location} is sunny with a temperature of 25°C."

if __name__ == "__main__":
    mcp.run(transport="streamable-http")  # Start the FastMCP server