# Agent Builder Agent – Google ADK Multi-Agent AI Solution Architect

## Kaggle 5-Day AI Agents Intensive Capstone Project

**Author:** Monica Das

---

# Problem Statement

Building modern AI applications requires much more than selecting a Large Language Model (LLM). Developers must make architectural decisions regarding multi-agent design, Retrieval-Augmented Generation (RAG), Model Context Protocol (MCP), memory, external tools, security, deployment, and project organization.

These decisions are often difficult for beginners and even experienced developers because they involve many interdependent technologies.

The goal of this project is to build an intelligent multi-agent AI Solution Architect that interviews users, understands their project requirements, recommends a production-ready AI architecture, and demonstrates real Model Context Protocol (MCP) integration through a custom FastMCP server.

---

# Project Overview

Agent Builder Agent is a multi-agent AI application developed using Google's Agent Development Kit (ADK) and Gemini 2.5 Flash.

Rather than functioning as a simple chatbot, the system behaves like an AI Solutions Architect.

It interviews the user, analyzes project requirements, evaluates technical trade-offs, recommends architecture decisions, performs security analysis, suggests Model Context Protocol (MCP) integrations, recommends deployment strategies, and generates an appropriate starter project structure.

The project also demonstrates a working FastMCP server integrated with Google ADK through the MCP Agent.

---

# Why I Chose This Project

I wanted to build something more practical than a conversational chatbot.

My objective was to create an intelligent AI Solution Architect capable of interviewing developers, understanding project requirements, coordinating multiple specialized agents, and producing production-ready recommendations.

Throughout this capstone I progressively evolved the system from a single interview agent into a coordinated multi-agent application using Google's Agent Development Kit (ADK).

This project also strengthened my practical skills in:

- Ubuntu Linux
- Python
- Google ADK
- FastMCP
- Git and GitHub
- Multi-agent orchestration
- Prompt engineering
- AI system architecture

---

# Multi-Agent Architecture

The application consists of a Root Agent that coordinates several specialized agents.

The workflow is:

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

Each agent focuses on a single responsibility before handing control to the next specialized agent.

---

# Agent Responsibilities

### Interview Agent

Collects project requirements by interviewing the user.

Examples include:

- Project purpose
- Target users
- Deployment preference
- Budget
- Expected scale
- Technology preferences

---

### Architecture Agent

Recommends:

- Single-agent vs multi-agent architecture
- LLM selection
- Memory strategy
- Retrieval-Augmented Generation (RAG)
- Vector databases
- Backend technologies
- Frontend technologies
- Deployment strategy

---

### Security Agent

Evaluates:

- Authentication
- Authorization
- Prompt Injection
- API security
- Encryption
- Privacy
- Responsible AI
- Sensitive information handling

The Security Agent also prioritizes risks and recommends mitigation strategies.

---

### MCP Agent

The MCP Agent recommends Model Context Protocol (MCP) integrations based on the user's project requirements.

In addition, this capstone demonstrates a real FastMCP server integration.

A custom FastMCP server (`medical_exam_server.py`) exposes the tool:

```
get_exam_info(exam_name)
```

The MCP Agent connects to this server through Google's ADK `McpToolset`.

When appropriate, the agent invokes the MCP tool and receives structured data including:

- Exam name
- Country
- Purpose
- Official information sources

The returned structured information is incorporated into the agent's final response.

This demonstrates real MCP tool execution rather than prompt-only simulation.

---

### Scaffold Agent

Recommends a production-ready project structure including:

- app/
- agents/
- tools/
- prompts/
- config/
- memory/
- rag/
- tests/
- docs/

It also recommends:

- Dockerfile
- requirements.txt
- README
- .env.example

---

# Workflow

The overall workflow is:

User Idea

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

---

# Major Features

- Interactive project interview
- Intelligent architecture recommendation
- Multi-agent orchestration
- Single-agent vs multi-agent analysis
- Retrieval-Augmented Generation (RAG) planning
- Memory recommendation
- Security analysis
- Model Context Protocol (MCP) planning
- Real FastMCP integration
- Project scaffold generation
- Deployment recommendation
- Technology stack recommendation
- Final AI architecture report

---

# Technologies Used

- Python
- Google Agent Development Kit (ADK)
- Gemini 2.5 Flash
- FastMCP
- Google ADK McpToolset
- Git
- GitHub
- Ubuntu Linux

---

# Demonstrated MCP Integration

The project includes a working FastMCP server.

The server provides a custom tool:

```
get_exam_info(exam_name)
```

The MCP Agent connects to the server using Google's ADK `McpToolset`.

A demonstration included:

- Requesting information about MCAT.
- The MCP Agent invoking the FastMCP server.
- The server returning structured information.
- The agent presenting the returned information and official source link to the user.

This confirms successful MCP tool execution within the Google ADK multi-agent workflow.

---

# What I Learned

Through this capstone I learned:

- Building multi-agent AI systems
- Agent orchestration
- Agent handoffs
- Prompt engineering
- AI system architecture
- Model Context Protocol (MCP)
- FastMCP server development
- Google ADK MCP integration
- Retrieval-Augmented Generation (RAG)
- Security considerations for AI applications
- Git and GitHub workflows
- Developing AI projects on Ubuntu Linux

---

# Future Improvements

Future versions of this project may include:

- Automatic project code generation
- Automatic README generation
- Persistent long-term memory
- Integration with additional production MCP servers
  - Google Drive
  - Gmail
  - GitHub
  - Slack
  - Databases
- Vector database integration
- One-click cloud deployment
- Automatic Docker generation
- Project ZIP generation

---

# Conclusion

This project demonstrates how multiple specialized AI agents can collaborate to design production-ready AI systems.

Instead of functioning as a single chatbot, Agent Builder Agent coordinates multiple expert agents to perform project interviews, architecture recommendation, security analysis, Model Context Protocol (MCP) planning, deployment advice, project scaffolding, and real MCP tool integration.

The implementation also demonstrates successful integration of Google's Agent Development Kit (ADK) with a custom FastMCP server, enabling actual tool execution within the multi-agent workflow.

The result is an intelligent AI Solution Architect that helps developers transform an initial idea into a well-structured, production-oriented AI system.

---

## GitHub Repository

https://github.com/RiseAgain11/agent-builder-adk-capstone
