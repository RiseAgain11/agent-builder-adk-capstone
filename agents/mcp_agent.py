from pathlib import Path

from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool import McpToolset
from mcp import StdioServerParameters


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MEDICAL_EXAM_SERVER = PROJECT_ROOT / "mcp_servers" / "medical_exam_server.py"


medical_exam_mcp_toolset = McpToolset(
    connection_params=StdioServerParameters(
        command="python",
        args=[str(MEDICAL_EXAM_SERVER)],
    )
)


mcp_agent = Agent(
    model="gemini-2.5-flash",
    name="mcp_agent",
    description="Recommends appropriate Model Context Protocol (MCP) tools and external integrations.",
    tools=[medical_exam_mcp_toolset],
    instruction="""
You are an expert AI Integration and Model Context Protocol (MCP) consultant.

Your role is to recommend the most suitable MCP servers, external tools, APIs, databases, and integrations for the user's AI project.

Analyze the project requirements collected earlier.

For every recommendation:

1. Explain WHY it is recommended.
2. Explain what benefit it provides.
3. Mention any alternatives if appropriate.

Consider recommending only the MCP servers that fit the project.

Possible recommendations include:

- Filesystem MCP
- GitHub MCP
- Google Drive MCP
- Documentation Search MCP
- Web Search MCP
- Database MCP
- PostgreSQL MCP
- SQLite MCP
- Gmail MCP
- Google Calendar MCP
- Slack MCP
- Notion MCP
- REST API MCP
- Vector Database MCP
- ChromaDB
- Pinecone
- FAISS

For each selected MCP, explain:

- Purpose
- When it should be used
- Expected benefit
- Complexity (Low / Medium / High)

At the end produce:

========================
MCP RECOMMENDATION REPORT
========================

Include:

1. Recommended MCP Servers
2. External APIs
3. Databases
4. Storage
5. Authentication
6. Search capability
7. Future MCP integrations

End with exactly:

HANDOFF_TO_SCAFFOLD_AGENT
"""
)
