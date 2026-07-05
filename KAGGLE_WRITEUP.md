# Agent Builder Agent – Google ADK Multi-Agent AI Solution Architect

## Kaggle 5-Day AI Agents Intensive Capstone Project

**Author:** Monica Das

---

# Problem Statement

Designing an AI agent is no longer as simple as selecting a Large Language Model (LLM). Developers must decide whether to use Retrieval-Augmented Generation (RAG), Model Context Protocol (MCP), memory, multiple specialized agents, external tools,
 databases, cloud deployment, and security mechanisms.

Many beginners struggle to make these architectural decisions.

The goal of this project is to build an intelligent AI consultant that interviews users, understands their requirements, and recommends a complete production-ready AI architecture.

---

# Project Overview

Agent Builder Agent is a multi-agent AI system developed using Google's Agent Development Kit (ADK).

Rather than simply answering questions, the system behaves like an AI Solutions Architect.

It interviews the user, analyzes project requirements, evaluates technical trade-offs, and generates recommendations covering architecture, security, MCP integration, deployment strategy, and starter project scaffolding.

---

# Why I Chose This Project

I wanted to build more than a chatbot. My goal was to create an AI Solution Architect capable of interviewing users, understanding project requirements, and recommending an appropriate AI system design.

Throughout this capstone I progressively enhanced the system from a simple interview agent into a coordinated multi-agent application using Google's Agent Development Kit (ADK). Each specialized agent contributes expertise in architecture,
 security, Model Context Protocol (MCP), and project scaffolding before producing a comprehensive solution report.

This project also strengthened my practical skills in Ubuntu Linux, Git, GitHub, prompt engineering, multi-agent orchestration, and AI application design.
---

# Multi-Agent Design

The project consists of several specialized AI agents coordinated by a Root Agent.

These include:

- Interview Agent
- Architecture Agent
- Security Agent
- MCP Advisor Agent
- Scaffold Agent

Each agent focuses on a specific responsibility before handing control to the next agent.

---

# Workflow

User Idea

↓

Interview Agent

↓

Architecture Agent

↓

Security Agent

↓

MCP Advisor Agent

↓

Scaffold Generator Agent

↓

Final Architecture Report

---

# Major Features

- Interactive project interview
- Intelligent architecture recommendations
- Single-agent vs multi-agent analysis
- RAG recommendation
- Memory recommendation
- Model Context Protocol (MCP) planning
- Security analysis
- Deployment recommendation
- Technology stack recommendation
- Project scaffold generation
- Final architecture report

---

# Model Context Protocol (MCP)

A dedicated MCP Advisor Agent evaluates whether external integrations are appropriate for the proposed AI system.

Possible recommendations include:

- Google Calendar
- Google Drive
- Gmail
- Learning Management Systems
- REST APIs
- Vector Databases
- Enterprise integrations

Rather than recommending MCP for every project, the system explains when MCP adds value and when it is unnecessary.

---

# Security

The Security Agent evaluates:

- Authentication
- Authorization
- Prompt Injection
- API security
- Encryption
- Privacy
- Responsible AI
- Sensitive information handling

The agent also assigns priorities and recommends mitigation strategies.

---

# Project Scaffold

The Scaffold Agent recommends a production-ready project structure including:

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

# Technologies Used

- Python
- Google Agent Development Kit (ADK)
- Gemini 2.5 Flash
- Git
- GitHub

---

# What I Learned

Through this capstone I learned:

- Building multi-agent AI systems
- Agent orchestration
- Agent handoffs
- Prompt engineering
- AI system architecture
- Model Context Protocol (MCP)
- Retrieval-Augmented Generation (RAG)
- Security considerations for AI applications
- Git and GitHub workflows
- Developing AI projects on Ubuntu Linux

---

# Future Improvements

Future versions of this project will include:

- Automatic project code generation
- Automatic README generation
- Persistent memory
- Live MCP server integrations
- Vector database integration
- One-click cloud deployment
- Automatic Docker generation
- Project ZIP generation

---

# Conclusion

This project demonstrates how specialized AI agents can collaborate to design complete AI solutions.

Instead of functioning as a single chatbot, the Agent Builder coordinates multiple expert agents to provide architecture guidance, security recommendations, MCP planning, deployment advice, and project scaffolding.

The result is an intelligent AI Solution Architect that helps developers transform an initial idea into a production-oriented design.

---

## GitHub Repository

https://github.com/RiseAgain11/agent-builder-adk-capstone
