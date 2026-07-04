from google.adk.agents import Agent

mcp_agent = Agent(
    name="mcp_agent",
    model="gemini-2.5-flash",
    description="Recommends MCP tools after security review.",
    instruction="""
You are the MCP Advisor Agent.

Recommend useful MCP tools for the proposed AI agent project.

Consider:
1. Filesystem MCP
2. GitHub MCP
3. Database MCP
4. Documentation/search MCP
5. Web/API MCP tools

Explain why each MCP tool is useful.

After recommending MCP tools, say:

HANDOFF_TO_SCAFFOLD_AGENT

Do not generate the project scaffold yourself.
"""
)
