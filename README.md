# Agent Builder Agent (Google ADK + MCP + Hybrid LLM)

## Overview

Agent Builder Agent is a multi-agent AI system built using Google's Agent Development Kit (ADK). It helps users design agentic AI applications by collecting requirements and recommending architectures, security practices, MCP tools, and starter project structures.

This project was developed as a Kaggle Capstone project.

---

# Features

- Google ADK multi-agent architecture
- Five specialist AI agents
- Interactive web interface using ADK Web
- Gemini 2.5 Flash integration
- MCP-aware recommendations
- Hybrid architecture prepared for OpenAI fallback
- Beginner-friendly project guidance

---

# Agent Architecture

```
                Agent Builder Root

                        │

        ┌───────────────┼───────────────┐

                        │

                Interview Agent

                        │

             (collect requirements)

                        │

            Architecture Agent

                        │

             Security Agent

                        │

                MCP Advisor

                        │

             Scaffold Generator
```

---

# Specialist Agents

## Interview Agent

Collects project requirements including:

- Project idea
- Domain
- Users
- RAG requirements
- Memory requirements
- Deployment preference

---

## Architecture Agent

Recommends:

- Single-agent vs Multi-agent
- Tools
- APIs
- Databases
- Memory
- RAG
- Deployment

---

## Security Agent

Reviews:

- Prompt injection
- Secret leakage
- Unsafe tool usage
- Privacy
- Human approval

---

## MCP Advisor Agent

Recommends Model Context Protocol tools including:

- Filesystem MCP
- GitHub MCP
- Database MCP
- Documentation Search MCP
- Web/API MCP

---

## Scaffold Generator

Produces starter project recommendations including:

- Folder structure
- Python modules
- Docker
- README
- Environment variables

---

# Technologies Used

- Python
- Google ADK
- Gemini 2.5 Flash
- MCP Concepts
- Gradio Prototype
- Ubuntu Linux

---

# Current Workflow

User

↓

Root Agent

↓

Interview Agent

↓

Architecture Recommendation

↓

Security Review

↓

MCP Recommendations

↓

Project Scaffold

---

# Running the Project

Activate environment

```bash
source ../.venv/bin/activate
```

Run

```bash
adk web
```

Open

```
http://127.0.0.1:8000
```

---

# Future Improvements

- Automatic multi-agent orchestration
- OpenAI fallback router
- Docker deployment
- Cloud deployment
- GitHub MCP integration
- Database MCP integration
- Authentication
- Persistent memory

---

# Author

Monica Das

Kaggle Google ADK Capstone Project

2026
