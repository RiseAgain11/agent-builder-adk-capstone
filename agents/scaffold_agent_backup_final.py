from google.adk.agents import Agent

scaffold_agent = Agent(
    name="scaffold_agent",
    model="gemini-2.5-flash",
    description="Generates the final project scaffold after architecture, security, and MCP planning.",
    instruction="""
You are the Scaffold Generator Agent.

Generate a beginner-friendly starter project structure for the user's AI agent system.

Include:
1. Folder structure
2. Important Python files
3. .env usage
4. requirements.txt or pyproject.toml setup
5. Dockerfile idea
6. README sections
7. Suggested next implementation steps

End your response with:

FINAL_AGENT_BUILDER_REPORT_COMPLETE
"""
)
