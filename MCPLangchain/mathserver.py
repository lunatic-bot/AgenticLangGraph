from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.tool
def subtract(a: int, b: int) -> int:
    """Subtract two numbers."""
    return a - b

@mcp.tool
def multuply(a: int, b: int) -> int:
    """multiply two numbers."""
    return a * b

## the tranposrt="stdio" tells server to use stdin and stdout to recieve and respond tool function calls
if __name__ == "__main__":
    mcp.run(transport="Stdio")