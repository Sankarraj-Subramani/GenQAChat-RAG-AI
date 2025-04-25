# GenQAChat Frontend

This is the React + Tailwind CSS frontend for **GenQAChat**, an AI-powered QA Knowledge Assistant. It connects to a FastAPI backend and allows users to ask questions related to test automation tools (like Selenium, Appium, Cypress, Jenkins, etc.) powered by a RAG (Retrieval-Augmented Generation) architecture.

---

## 📦 Tech Stack

- **Next.js (React)** – for building UI
- **Tailwind CSS** – for responsive styling
- **react-markdown** – to render markdown answers
- **rehype-highlight** – syntax highlighting in answers
- **remark-gfm** – GitHub Flavored Markdown support
- **FastAPI backend** – hosted on a separate port

---

## 🚀 How to Run the Frontend

### 1. Install dependencies

```bash
cd frontend
npm install
```

### 2. Start the development server

```bash
npm run dev
```

Access the app at: `http://localhost:3000`

---

## 🔗 Backend Integration

Make sure the FastAPI backend is running at:

```
http://localhost:8000/query
```

In `frontend/pages/index.tsx`, the fetch URL must match your backend endpoint:

```ts
const res = await fetch('http://localhost:8000/query', {
  method: 'POST',
  ...
});
```

Update this URL when deploying or testing with Codespaces.

---

## 🧠 Features

- Asks natural language questions like:  
  *“How to add dependencies in Selenium?”*  
  *“What is an XPath locator?”*

- Receives markdown-based answers from the FastAPI backend.
- Renders styled output with code snippets, tables, and bullet points.

---

## 💡 Enhancements Coming Soon

- Chat history
- Document upload
- Tool-specific filtering
- AI-powered follow-ups

---

## 👤 Author

Created by [Sankarraj Subramani](https://github.com/Sankarraj-Subramani)

---