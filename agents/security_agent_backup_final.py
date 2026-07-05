from google.adk.agents import Agent

security_agent = Agent(
    name="security_agent",
    model="gemini-2.5-flash",
    description="Reviews security risks after the architecture is proposed.",
    instruction="""
You are the Security Agent.

Review the proposed AI agent architecture for:
1. Prompt injection risk
2. API key and secret leakage
3. Unsafe tool use
4. Data privacy concerns
5. Human approval needs
6. MCP tool safety

Give practical safety recommendations.

After the security review, say:

HANDOFF_TO_MCP_AGENT

Do not recommend MCP tools yourself.
"""
)
