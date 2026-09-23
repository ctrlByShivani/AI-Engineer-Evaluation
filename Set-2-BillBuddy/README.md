# BillBuddy 💰

BillBuddy is an AI-powered bill and expense assistant built using
Google Gemini and LangChain.

It understands the user's request and selects the appropriate tool
to complete the task.

## Features

- Split a bill among multiple people
- Calculate tips and total bill
- AI-based tool selection
- Handles general questions without using a tool
- Handles invalid inputs gracefully
- Simple conversational interface

## Tools

### 1. Bill Splitter

The `split_bill` tool calculates how much each person should pay.

Example:

```text
Split ₹1800 between 4 people.

## How It Works

```text
User Request
     ↓
BillBuddy Agent
     ↓
Understand User Intent
     ↓
 ┌──────────────┬──────────────┐
 ↓              ↓              ↓
Bill Splitter   Tip Calculator  No Tool
 ↓              ↓              ↓
Result          Result          AI Response
 └──────────────┴──────────────┘
              ↓
         Final Response

## Technologies Used

- Python
- Google Gemini
- LangChain
- LangChain Google GenAI
- python-dotenv

## Project Structure

```text
BillBuddy/
│
├── main.py
├── agent.py
├── tools.py
├── prompts.py
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

## Setup

Follow these steps to run BillBuddy.

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd BillBuddy

## Error Handling

BillBuddy checks user inputs before performing calculations.

For example:

- Negative bill amounts are rejected.
- Negative tip percentages are rejected.
- Zero or negative number of people is rejected.

Example:

```text
Split ₹1800 between 0 people.

## Assignment

This project was developed for the **AI Agent with Tool Calling** assignment.

The project demonstrates:

- AI agent implementation
- Multiple tool definitions
- Tool selection based on user intent
- Tool execution
- Graceful error handling