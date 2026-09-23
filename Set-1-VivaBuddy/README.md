# VivaBuddy

## AI-Powered Viva Practice Assistant

VivaBuddy is an AI-powered conversational viva practice assistant designed for computer engineering students.

It allows students to select a subject and practice viva questions through a multi-turn conversation with an AI examiner.

## Features

* Subject-based viva practice
* AI-generated viva questions
* Student answer evaluation
* Score out of 10
* Feedback on answers
* Follow-up questions
* Conversation memory
* Multi-turn viva sessions
* Environment-based API key configuration
* Error handling for AI/API failures

## Technologies Used

* Python
* LangChain
* Google Gemini
* LangChain Google Generative AI
* python-dotenv

## Architecture

```text
Student
   ↓
VivaBuddy
   ↓
Subject Selection
   ↓
Prompt Template
   ↓
LangChain
   ↓
Google Gemini
   ↓
Question / Evaluation
   ↓
Conversation Memory
   ↓
Next Question
```

## Project Structure

```text
VivaBuddy/
├── main.py
├── prompts.py
├── memory.py
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup

### 1. Clone or download the project

Open the project folder in VS Code.

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the API key

Create a `.env` file:

```text
GOOGLE_API_KEY=your_gemini_api_key_here
```

Never share or upload the `.env` file.

### 6. Run VivaBuddy

```bash
python main.py
```

## Sample Interaction

```text
Enter your subject: DBMS

VivaBuddy:
What is normalization in DBMS?

Your answer:
Normalization is the process of organizing data
to reduce redundancy and improve data integrity.

VivaBuddy Evaluation:

Score: 8/10

Correctness: Correct

Feedback:
The answer correctly explains the purpose of
normalization. It could be improved by mentioning
normal forms such as 1NF, 2NF and 3NF.

Continue to next question? (yes/no): yes

VivaBuddy:
What is the difference between 2NF and 3NF?

Your answer:
...
```

## How It Works

1. The student enters a subject.
2. VivaBuddy generates a viva question using a prompt template.
3. The student provides an answer.
4. LangChain sends the question and answer to the Gemini model.
5. The AI evaluates the answer.
6. The evaluation is stored in conversation memory.
7. The previous conversation is provided when generating the next question.
8. VivaBuddy generates another question based on the student's previous performance.

## Purpose

VivaBuddy is designed to provide an interactive environment where students can practice explaining technical concepts and receive immediate AI-based feedback.
