# Agent Builder Agent
## Google ADK Multi-Agent AI Solution Architect

A multi-agent AI application built with **Google Agent Development Kit (ADK)** and **Gemini 2.5 Flash** that interviews users, recommends AI system architectures, performs security analysis, suggests Model Context Protocol (MCP) integrations, and generates production-ready project scaffolds.

This capstone also demonstrates **real FastMCP integration** using Google's ADK `McpToolset`.

---

# Features

- Multi-agent AI architecture
- Interactive project interview
- AI architecture recommendations
- Security analysis
- Model Context Protocol (MCP) recommendations
- Real FastMCP server integration
- Project scaffold generation
- Deployment recommendations

---

# Multi-Agent Workflow

```
User

↓

Interview Agent

↓

Architecture Agent

↓

Security Agent

↓

MCP Agent

↓

Scaffold Agent

↓

Final AI Solution Report
```

---

# Agents

## Interview Agent

Collects project requirements.

Examples:

- Project idea
- Users
- Budget
- Deployment
- Scale

---

## Architecture Agent

Recommends:

- Single vs Multi-Agent
- LLM
- Memory
- RAG
- Databases
- APIs
- Backend
- Frontend
- Deployment

---

## Security Agent

Evaluates:

- Authentication
- Authorization
- Prompt Injection
- Encryption
- Privacy
- Responsible AI

---

## MCP Agent

Recommends suitable Model Context Protocol (MCP) integrations.

This project also includes a **real FastMCP server**.

---

## Scaffold Agent

Generates a production-ready project structure.

---

# Real MCP Integration

The project demonstrates a working FastMCP server.

Server:

```
mcp_servers/medical_exam_server.py
```

Exposed MCP Tool:

```python
get_exam_info(exam_name)
```

Example:

```
get_exam_info("MCAT")
```

Returns:

- Exam name
- Country
- Purpose
- Official information sources

The MCP Agent accesses the tool through Google's ADK `McpToolset`.

During testing, the application successfully:

- transferred control to `mcp_agent`
- invoked `get_exam_info("MCAT")`
- received structured data from the MCP server
- incorporated the returned information into the final AI response

This demonstrates **real MCP tool execution** rather than prompt-only simulation.

---

# Technologies

- Python
- Google ADK
- Gemini 2.5 Flash
- FastMCP
- Google ADK McpToolset
- Git
- GitHub
- Ubuntu Linux

---

# Project Structure

```
agent_builder_adk/

├── agent.py
├── agents/
│   ├── interview_agent.py
│   ├── architecture_agent.py
│   ├── security_agent.py
│   ├── mcp_agent.py
│   └── scaffold_agent.py
│
├── mcp_servers/
│   └── medical_exam_server.py
│
├── data/
├── README.md
└── KAGGLE_WRITEUP.md
```

---

# Future Improvements

- Google Drive MCP
- GitHub MCP
- Gmail MCP
- Slack MCP
- Database MCP
- Cloud deployment
- Automatic code generation
- Long-term memory
- Multi-user support

---

# Capstone

Created as part of the **Kaggle 5-Day AI Agents Intensive Capstone Project** using Google's Agent Development Kit (ADK).

Author: **Monica Das**
