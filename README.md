# README.md

# GenQAChat-RAG-AI

<p align="center">
  <img src="https://i.postimg.cc/qqp9RSF2/Screenshot-2025-04-25-at-1-28-45-PM.png" alt="GenQAChat Logo" width="200"/>
</p>

**An AI-Powered Chatbot Assistant for QA Engineers**  
Created by [Sankarraj Subramani](https://github.com/Sankarraj-Subramani)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?template_repository=Sankarraj-Subramani/GenQAChat-RAG-AI)

---

## 🧠 Overview

**GenQAChat-RAG-AI** is a Generative AI-based chatbot built to assist QA engineers and automation testers with domain-specific questions.

It leverages:
- **LangChain** to structure QA retrievals
- **HuggingFace Sentence Transformers** for local embeddings (No OpenAI API needed!)
- **FAISS VectorStore** for semantic search
- **FastAPI** backend and **Next.js** frontend

---

## 💡 Example Use Cases

Ask your assistant:
- "How to write an XPath for a dynamic modal popup?"
- "Steps to configure Jenkins pipeline with GitHub?"
- "What’s the best way to implement page object model in Selenium?"

---

## 🔧 Tech Stack

| Layer         | Tech                     |
|---------------|---------------------------|
| Backend       | FastAPI, LangChain         |
| Embeddings    | HuggingFace MiniLM         |
| Vector Store  | FAISS (local)              |
| Frontend      | Next.js, React, TailwindCSS |
| Deployment    | GitHub Codespaces-ready    |

---

## ⚙️ Architecture

```
     ┌─────────────────────────────────────────────────────┐
         ┌────────────────────────────┐
         │     Next.js Frontend UI    │
         └────────────┬───────────────┘
                      │
                      ▼
          REST API (FastAPI backend)
                      │
                      ▼
    LangChain Retriever + HuggingFace Embeddings
                      │
                      ▼
         FAISS VectorStore (Semantic Search)
                      │
                      ▼
       Embedded QA Knowledge Base (Markdown/Text)
 └─────────────────────────────────────────────────────┘
```

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/Sankarraj-Subramani/GenQAChat-RAG-AI.git
cd GenQAChat-RAG-AI
```

### 2. Launch in GitHub Codespaces

Click the badge above ☝️ or visit:
[Launch in Codespaces](https://github.com/codespaces/new?template_repository=Sankarraj-Subramani/GenQAChat-RAG-AI)

### 3. Run Locally

#### Backend (FastAPI)
```bash
cd backend
pip install -r requirements.txt
python app/rag_chain.py    # ➡️ builds vectorstore.pkl
uvicorn app.main:app --reload
```

#### Frontend (Next.js)
```bash
cd ../frontend
npm install
npm run dev
```

### 4. No OpenAI Key Needed

This version uses **local HuggingFace embeddings** — no external API keys required!

---

## 🪩 Folder Structure

```
GenQAChat-RAG-AI/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   └── rag_chain.py
│   └── requirements.txt
├── frontend/
│   ├── pages/
│   │   └── index.tsx
│   └── ...
├── knowledge_base/
│   ├── selenium.md
│   ├── appium.md
│   ├── cypress.md
│   ├── playwright.md
│   ├── jenkins.md
│   └── xpaths.md
└── README.md
```

---

## 🧐 Knowledge Base

All QA knowledge lives inside `knowledge_base/` folder:
- Selenium
- Appium
- Cypress
- Playwright
- Jenkins Pipelines
- XPath Best Practices

These markdown files are **embedded into FAISS** for real-time QA answering.

---

## 🛠️ Built With

- [FastAPI](https://fastapi.tiangolo.com/)
- [LangChain](https://www.langchain.com/)
- [FAISS](https://faiss.ai/)
- [HuggingFace Transformers](https://huggingface.co/docs/transformers/index)
- [Next.js](https://nextjs.org/)

---

## 🏆 Contributions

Contributions are welcome!
- Add new knowledge base markdowns
- Improve UI/UX
- Suggest features like multiple file uploads, authentication

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## ✨ Author

**Sankarraj Subramani**  
QA Automation Lead | AI/ML Enthusiast | EB2-NIW/EB1A Aspirant  
[GitHub](https://github.com/Sankarraj-Subramani) • [LinkedIn](https://www.linkedin.com/in/sankarraj-subramani-34254757)

> If you like this project, kindly star the repo and share with the QA + AI community! ⭐


---

