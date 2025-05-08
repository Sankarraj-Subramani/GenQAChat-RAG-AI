# GenQAChat-RAG-AI
[![Open the output in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://genappchat-rag-ai-izvuchflvg3barx6mhj3xo.streamlit.app/)

<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1F7uyMPREOVJzgTOG0pWbX1yYnuGi-P2J" alt="GenQAChat Logo" width="200"/>
</p>


> **Empowering QA Engineers with AI**  
> A privacy-focused, offline-ready chatbot assistant that delivers instant answers to automation testing questions using open-source embeddings and RAG architecture.

---

## 🧠 Overview

**GenQAChat-RAG-AI** is a Generative AI-based chatbot built to assist QA engineers and automation testers with domain-specific questions.

It leverages:
- **LangChain** to structure QA retrievals
- **HuggingFace Sentence Transformers** for local embeddings (No OpenAI API needed!)
- **FAISS VectorStore** for semantic search
- **FastAPI** backend and **Next.js** frontend

> 🧪 **NIW-Aligned:** Demonstrates scalable, open-source QA innovation for critical infrastructure domains.

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

---

## 🗂️ Folder Structure

```plaintext
GenQAChat-RAG-AI/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI backend with /api/ask endpoint
│   │   └── rag_chain.py         # Builds vectorstore.pkl from markdowns
│   └── requirements.txt         # Python dependencies
├── frontend/
│   ├── pages/
│   │   └── index.tsx            # Next.js UI for asking QA questions
│   ├── components/              # (Optional) reusable UI components
│   ├── .env.local               # Contains NEXT_PUBLIC_BACKEND_URL
│   ├── next.config.js           # Dynamically resolves Codespace backend URL
│   └── package.json             # React + Tailwind app dependencies
├── knowledge_base/
│   ├── selenium.md              # QA content embedded into FAISS
│   ├── appium.md
│   ├── cypress.md
│   ├── playwright.md
│   ├── jenkins.md
│   └── xpaths.md
├── models/                      # Optional: HuggingFace cache
├── vectorstore.pkl              # Serialized FAISS store (auto-generated)
├── streamlit_app.py             # Streamlit UI for QA chatbot (optional deployment)
├── make_ports_public.sh         # CLI script to expose ports on Codespaces
├── devcontainer.json            # GitHub Codespaces automation config
├── requirements.txt             # Streamlit related requirements files
└── README.md                    # Project overview and instructions


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

## 🏆 Hackathon Submission

**Event:** Code for Change: AI Hackathon 2025  
**Category:** Ethical AI & Bias Mitigation / Social Good  
**Public Repo:** [github.com/Sankarraj-Subramani/GenQAChat-RAG-AI](https://github.com/Sankarraj-Subramani/GenQAChat-RAG-AI)

---
### 📢 Final Step (Auto-Public Port Setup)

If not already public, run this in terminal:

```bash
./make_ports_public.sh
```
[![Open in Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?template_repository=Sankarraj-Subramani/GenQAChat-RAG-AI)

## 🇺🇸 EB2-NIW Relevance

This project supports the U.S. national interest by:
- Enabling **secure, ethical automation** for healthcare, aviation, and public-sector QA.
- Providing **open-source QA intelligence** for underserved developers.
- Promoting **bias-free, reproducible testing guidance** using local LLMs.

---

## ✨ Author

**Sankarraj Subramani**  
QA Automation Lead | AI/ML Enthusiast | EB2-NIW/EB1A Aspirant  
[GitHub](https://github.com/Sankarraj-Subramani) • [LinkedIn](https://www.linkedin.com/in/sankarraj-subramani-34254757)

> ⭐ If you like this project, kindly star the repo and share with the QA + AI community!
