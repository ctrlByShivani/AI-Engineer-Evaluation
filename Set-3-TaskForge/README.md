# TaskForge — Multi-Agent Report Generation System

TaskForge is a multi-agent AI application that uses multiple specialized AI agents to collaboratively generate a structured report on a given topic.

The system divides the task into different roles such as planning, research, writing, and reviewing. Each agent performs a specific responsibility, and the Python workflow coordinates the overall process.

---

## Problem Statement

Generating a good report usually requires multiple steps such as understanding the task, collecting information, organizing the content, writing the report, and reviewing it.

TaskForge demonstrates how these steps can be divided among multiple AI agents so that each agent focuses on a specific responsibility.

---

## Objective

The main objective of TaskForge is to demonstrate a practical **Multi-Agent System** where:

- Multiple AI agents collaborate on a common task.
- Each agent has a clearly defined role.
- Information is passed from one agent to another.
- The overall workflow is coordinated programmatically.
- The final output is reviewed before being presented to the user.

---

## Features

- Multi-agent AI workflow
- Four specialized AI agents
- Coordinator-based task planning
- Research generation
- Structured report writing
- Automated report review
- Gemini-powered responses
- Environment-variable based API key configuration
- Basic error handling
- Interactive command-line interface

---

## Multi-Agent Architecture

```text
                    USER
                      |
                      v
              +---------------+
              |  COORDINATOR  |
              |   Agent       |
              +---------------+
                      |
                 Task Plan
                      |
                      v
              +---------------+
              |  RESEARCHER   |
              |     Agent     |
              +---------------+
                      |
                  Research
                      |
                      v
              +---------------+
              |    WRITER     |
              |     Agent     |
              +---------------+
                      |
                Draft Report
                      |
                      v
              +---------------+
              |   REVIEWER    |
              |     Agent     |
              +---------------+
                      |
                      v
              FINAL REPORT