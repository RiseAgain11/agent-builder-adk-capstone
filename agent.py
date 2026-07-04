from google.adk.agents.llm_agent import Agent

from .agents.interview_agent import interview_agent
from .agents.architecture_agent import architecture_agent
from .agents.security_agent import security_agent
from .agents.mcp_agent import mcp_agent
from .agents.scaffold_agent import scaffold_agent


root_agent = Agent(
    model="gemini-2.5-flash",
    name="agent_builder_root",
    description="A Google ADK multi-agent system that helps users design agentic AI projects.",
    instruction="""
You are Agent Builder Root Coordinator.

Your job is to coordinate five specialist agents:

1. interview_agent
2. architecture_agent
3. security_agent
4. mcp_agent
5. scaffold_agent

Workflow:
- Start with interview_agent.
- When interview_agent says HANDOFF_TO_ARCHITECTURE_AGENT, transfer to architecture_agent.
- When architecture_agent says HANDOFF_TO_SECURITY_AGENT, transfer to security_agent.
- When security_agent says HANDOFF_TO_MCP_AGENT, transfer to mcp_agent.
- When mcp_agent says HANDOFF_TO_SCAFFOLD_AGENT, transfer to scaffold_agent.
- When scaffold_agent says FINAL_AGENT_BUILDER_REPORT_COMPLETE, summarize the final result briefly.

Do not skip the workflow unless the user explicitly asks for a specific specialist agent.

Be clear, practical, beginner-friendly, and implementation-oriented.
""",
    sub_agents=[
        interview_agent,
        architecture_agent,
        security_agent,
        mcp_agent,
        scaffold_agent,
    ],
)
