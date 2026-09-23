# AI Engineer Evaluation

This repository contains three AI engineering assignments completed as part of the **AI Engineer Technical Evaluation Program**.

The projects demonstrate different AI engineering concepts including **LangChain, Google Gemini, tool calling, memory, prompt engineering, and multi-agent systems**.

---

## 📂 Repository Structure

```text
AI-Engineer-Evaluation/
│
├── Set-1-VivaBuddy/
│   ├── main.py
│   ├── prompts.py
│   ├── memory.py
│   ├── requirements.txt
│   ├── README.md
│   ├── .env.example
│   └── .gitignore
│
├── Set-2-BillBuddy/
│   ├── main.py
│   ├── agent.py
│   ├── tools.py
│   ├── prompts.py
│   ├── requirements.txt
│   ├── README.md
│   ├── .env.example
│   └── .gitignore
│
├── Set-3-TaskForge/
│   ├── main.py
│   ├── agents.py
│   ├── prompts.py
│   ├── requirements.txt
│   ├── README.md
│   ├── .env.example
│   └── .gitignore
│
└── .gitignore
```

---

# 🚀 Projects

## 1. VivaBuddy — AI Viva Practice Assistant

**Assignment:** Set 1

VivaBuddy is an AI-powered viva practice assistant designed to help students prepare for technical viva examinations.

### Key Features

* Generates technical viva questions
* Provides AI-generated answers
* Uses prompt engineering for structured responses
* Maintains conversational memory
* Uses Google Gemini through LangChain
* Provides an interactive command-line interface

### Technologies

* Python
* LangChain
* Google Gemini
* python-dotenv

### Main Components

| File               | Purpose                        |
| ------------------ | ------------------------------ |
| `main.py`          | Runs the VivaBuddy application |
| `prompts.py`       | Contains AI prompts            |
| `memory.py`        | Handles conversation memory    |
| `requirements.txt` | Project dependencies           |

📁 **Project:** [`Set-1-VivaBuddy`](./Set-1-VivaBuddy)

---

# 2. BillBuddy — AI Bill & Expense Assistant

**Assignment:** Set 2**

BillBuddy is an AI-powered bill and expense assistant that understands user requests and decides whether a calculation tool is required.

### Available Tools

#### Split Bill

Calculates how much each person should pay when a bill is divided among multiple people.

#### Calculate Tip

Calculates the tip amount based on the bill amount and selected tip percentage.

### Key Features

* AI-based intent understanding
* Tool selection
* Bill splitting
* Tip calculation
