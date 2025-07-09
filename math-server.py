from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math-Server")


@mcp.tool("add")
def add(a: int, b: int) -> int:
    """Adds two integers.""" #Based on this llm will understand which tool to call
    return a + b

@mcp.tool("subtract")
def subtract(a: int, b: int) -> int:
    """Subtracts the second integer from the first."""
    return a - b

@mcp.tool("multiply")
def multiply(a: int, b: int) -> int:    
    """Multiplies two integers."""
    return a * b    

@mcp.tool("divide")
def divide(a: int, b: int) -> float:
    """Divides the first integer by the second."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    mcp.run(transport="stdio")  # Start the FastMCP server
    
# The tranport = "stdio" allows the server to communicate via standard input/output (stdin/stdout),
# to receive and respond to tool function calls.