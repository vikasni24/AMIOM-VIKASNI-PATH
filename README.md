

# AI Self-Correcting Python Debugger

An intelligent web-based debugging tool that automatically detects and fixes Python code errors using AI.

---

## Overview

Debugging can be frustrating and time-consuming—especially when error messages are unclear. This project simplifies that process by combining code execution with AI-powered correction.

Just paste your Python code, and the system will:

* Run it
* Detect errors
* Automatically generate a corrected version

No more digging through StackOverflow tabs.

---

## How It Works

1. User submits Python code via the frontend
2. Backend executes the code in a controlled environment
3. If an error occurs:

   * Traceback is captured
   * Code + error is sent to AI
4. AI returns a corrected version of the code
5. Both error and fixed code are displayed

---

## Architecture

```
User → Frontend (Next.js) → Backend (FastAPI)
     → Code Execution Engine → AI Fixer → Response
```

### Components

* **Code Runner**: Executes Python code
* **Error Handler**: Captures output and errors
* **AI Fixer**: Sends data to AI and retrieves fixes

---

## Tech Stack

### Frontend

* Next.js
* TypeScript
* HTML, CSS

### Backend

* FastAPI
* Python

### AI Integration

* Groq API

---

## API

### `POST /api/debug`

**Request**

```json
{
  "code": "print('Hello)",
  "model": "model_name"
}
```

**Response**

```json
{
  "error": "SyntaxError: EOL while scanning string literal",
  "fixed_code": "print('Hello')"
}
```

---


## Setup & Installation

### Prerequisites

Make sure you have:

* Python 3.8+
* Node.js (v18+ recommended)
* npm or yarn
* Groq API Key
* Uvicorn

---

## Installation

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <project-folder>
```

---

### 2. Backend Setup (FastAPI)

```bash
# Create virtual environment
python -m venv .venv

# Activate it
# Mac/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

### 3. Set Environment Variables

Create a `.env` file or export manually:

```bash
export GROQ_API_KEY="your_api_key_here"
```

(Yeah… without this your AI becomes emotionally unavailable)

---

### 4. Frontend Setup (Next.js)

```bash
cd frontend
npm install
cd ..
```

---

## Running the Application

You need **two terminals**.

---

### Terminal 1 — Start Backend

```bash
source .venv/bin/activate
uvicorn self_correction_agent.api_server:app --reload --port 8000
```

Backend runs at:
`http://localhost:8000`

---

### Terminal 2 — Start Frontend

```bash
cd frontend
npm run dev
```

Frontend runs at:
`http://localhost:3000`

---

## How to Use

1. Open `http://localhost:3000`
2. Paste your Python code
3. Click **Run & Debug**
4. See:

   * Error output
   * AI-corrected code

## Features

* Automatic error detection
* AI-powered code correction
* Real-time debugging feedback
* Clean dual-panel UI
* Modular and scalable design

---

## Problem It Solves

* Debugging is slow and repetitive
* Error messages are hard to understand
* Too much dependency on external resources
* Context switching kills productivity

---

## Results

* Successfully detects syntax & runtime errors
* Generates corrected code instantly
* Reduces debugging time significantly
* Helps beginners learn faster

---

## Challenges

* Safe execution of user-submitted code
* Handling unpredictable AI responses
* Managing API latency
* Designing intuitive UI

---

## Future Improvements

* Multi-language support
* AI explanations (not just fixes)
* VS Code / IDE integration
* Smarter reasoning models
* Real-time collaborative debugging

---

## Conclusion

This project shows how AI can move debugging from a manual struggle to an automated, intelligent workflow saving time and actually helping developers learn instead of just fixing errors blindly.

---

## References

* Python Documentation
* FastAPI Docs
* Next.js Docs
* Groq API Docs

