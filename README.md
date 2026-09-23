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
* Direct conversational responses
* Invalid input handling
* Google Gemini integration

### Technologies

* Python
* LangChain
* Google Gemini
* Python-dotenv

### Main Components

| File               | Purpose                                 |
| ------------------ | --------------------------------------- |
| `main.py`          | Runs the application                    |
| `agent.py`         | Handles AI agent logic                  |
| `tools.py`         | Contains bill and tip calculation tools |
| `prompts.py`       | Contains AI prompts                     |
| `requirements.txt` | Project dependencies                    |

📁 **Project:** [`Set-2-BillBuddy`](./Set-2-BillBuddy)

---

# 3. TaskForge — Multi-Agent Report Generation System

**Assignment:** Set 3 — L3-01 Multi-Agent System

TaskForge is a multi-agent AI system in which multiple specialized AI agents collaborate to create a structured report.

### Multi-Agent Architecture

```text
                    USER
                      │
                      ▼
                COORDINATOR
                      │
                      ▼
                 Task Plan
                      │
                      ▼
                 RESEARCHER
                      │
                      ▼
                  Research
                      │
                      ▼
                   WRITER
                      │
                      ▼
                Draft Report
                      │
                      ▼
                  REVIEWER
                      │
                      ▼
             Final Polished Report
```

### Agent Roles

| Agent           | Responsibility                             |
| --------------- | ------------------------------------------ |
| **Coordinator** | Creates the task execution plan            |
| **Researcher**  | Collects and organizes useful information  |
| **Writer**      | Converts research into a structured report |
| **Reviewer**    | Reviews and improves the final report      |

### Workflow

1. The user provides a topic.
2. The **Coordinator Agent** creates a task plan.
3. The **Researcher Agent** gathers and organizes information.
4. The **Writer Agent** creates a structured report.
5. The **Reviewer Agent** checks and improves the report.
6. TaskForge displays the final polished report.

### Technologies

* Python
* LangChain
* Google Gemini
* Multi-Agent Architecture
* Prompt Engineering
* python-dotenv

### Main Components

| File               | Purpose                        |
| ------------------ | ------------------------------ |
| `main.py`          | Controls the complete workflow |
| `agents.py`        | Creates the AI agents          |
| `prompts.py`       | Contains role-specific prompts |
| `requirements.txt` | Project dependencies           |

📁 **Project:** [`Set-3-TaskForge`](./Set-3-TaskForge)

---

# 🛠️ Technologies Used

The three assignments use the following technologies and concepts:

* **Python**
* **LangChain**
* **Google Gemini**
* **Prompt Engineering**
* **AI Agents**
* **Tool Calling**
* **Conversation Memory**
* **Multi-Agent Systems**
* **Environment Variables**

---

# 🔐 Environment Variables

API keys are stored locally in `.env` files and are **not included in this repository**.

Each project contains an `.env.example` file showing the required environment variable format.

For example:

```env
GOOGLE_API_KEY=your_api_key_here
```

Create a `.env` file inside the respective project folder and add your own API key.

**Never commit your actual API key to GitHub.**

---

# ▶️ Running the Projects

Each assignment is self-contained and has its own `README.md` containing project-specific setup and execution instructions.

General workflow:

```bash
cd Set-1-VivaBuddy
```

or

```bash
cd Set-2-BillBuddy
```

or

```bash
cd Set-3-TaskForge
```

Then install the required dependencies:

```bash
pip install -r requirements.txt
```

Create the required `.env` file using the corresponding `.env.example`.

Finally, run:

```bash
python main.py
```

---

# 📋 Evaluation Mapping

| Assignment    | Project   | Main AI Concept         |
| ------------- | --------- | ----------------------- |
| Set 1         | VivaBuddy | AI Assistant + Memory   |
| Set 2         | BillBuddy | AI Agent + Tool Calling |
| Set 3 — L3-01 | TaskForge | Multi-Agent System      |

---

# 🎯 Objective

The purpose of this repository is to demonstrate practical implementation of AI engineering concepts through three progressively different applications:

**AI Assistant → AI Agent with Tools → Multi-Agent System**

Each project focuses on a specific aspect of building practical AI-powered applications using Python, LangChain, and Google Gemini.

---

# 👩‍💻 Author

**Shivani**

Computer Engineering Student

GitHub: [@ctrlByShivani](https://github.com/ctrlByShivani)

---

## 📄 License

This repository was created for educational and evaluation purposes.
