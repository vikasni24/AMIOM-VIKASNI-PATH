<<<<<<< HEAD
This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
=======


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

### Other Tools

* Subprocess module
* CORS Middleware

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

This project shows how AI can move debugging from a manual struggle to an automated, intelligent workflow—saving time and actually helping developers learn instead of just fixing errors blindly.

---

## References

* Python Documentation
* FastAPI Docs
* Next.js Docs
* Groq API Docs

>>>>>>> 6c3264fa23546a5f7e4a1a81a1868ec4a2ab8de6
