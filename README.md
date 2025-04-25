# GenQAChat-RAG-AI

<p align="center">
  <img src="(https://i.postimg.cc/qqp9RSF2/Screenshot-2025-04-25-at-1-28-45-PM.png)](https://postimg.cc/7GQBtswL)" alt="GenQAChat Logo" width="200"/>
</p>

**An AI-Powered Chatbot Assistant for QA Engineers**  
Created by [Sankarraj Subramani](https://github.com/Sankarraj-Subramani)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?template_repository=Sankarraj-Subramani/GenQAChat-RAG-AI)

---

## 🧠 Overview

**GenQAChat-RAG-AI** is a Generative AI-based chatbot built to assist QA engineers and automation testers with domain-specific questions.

It leverages:
- **LangChain** to structure LLM interactions  
- **OpenAI (GPT-4)** for natural language understanding  
- **ChromaDB** for fast semantic search over QA documentation  
- **RAG (Retrieval-Augmented Generation)** to make the LLM responses accurate and grounded

---

## 💡 Example Use Cases

Ask your assistant:
- “How to write an XPath for a dynamic modal popup?”  
- “Steps to configure Jenkins pipeline with GitHub?”  
- “What’s the best way to implement page object model in Selenium?”

---

## 🔧 Tech Stack

| Layer         | Tech                     |
|---------------|--------------------------|
| Backend       | FastAPI, LangChain       |
| AI Model      | OpenAI GPT-4             |
| Vector DB     | ChromaDB (embeddings)    |
| Frontend      | Next.js, React, TailwindCSS |
| Deployment    | GitHub Codespaces-ready  |

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
    LangChain QA Chain + OpenAI API
                      │
                      ▼
         ChromaDB (QA Vector Store)
                      │
                      ▼
       Embedded QA Knowledge Base
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
uvicorn app.main:app --reload
```

#### Frontend (Next.js)
```bash
cd ../frontend
npm install
npm run dev
```

### 4. Add OpenAI API Key

Create a `.env` file inside the `backend/` folder:

```env
OPENAI_API_KEY=your-openai-key-here
```

---

## 🧹 Folder Structure

```
GenQAChat-RAG-AI/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   └── rag_chain.py
│   └── requirements.txt
├── frontend/
│   ├── pages/
│   ├── components/
│   └── ...
├── knowledge_base/
│   ├── xpaths.txt
│   ├── selenium.md
│   └── jenkins_pipeline.txt
└── README.md
```

---

## 🧠 Knowledge Base

All your QA knowledge lives inside the `knowledge_base/` folder.

You can add:
- Automation FAQs  
- XPath tricks  
- Setup/config guides  
- Selenium/Cypress/Appium tutorials

These files are embedded into ChromaDB for semantic search and intelligent LLM-powered answers.

---

## 🔪 Built With

- [FastAPI](https://fastapi.tiangolo.com/)
- [LangChain](https://www.langchain.com/)
- [ChromaDB](https://www.trychroma.com/)
- [OpenAI GPT-4](https://platform.openai.com/)
- [Next.js](https://nextjs.org/)

---

## 🏆 Contributions

Contributions are welcome!

You can:
- Add new markdown/text files to the knowledge base  
- Suggest UI/UX improvements  
- Propose new features (e.g., file upload, code analysis, voice input)

---

## 📄 License

MIT License – free to use, modify, and distribute.

---

## ✨ Author

**Sankarraj Subramani**  
QA Automation Lead | AI/ML Enthusiast | EB2-NIW/EB1A Aspirant  
[GitHub](https://github.com/Sankarraj-Subramani) • [LinkedIn](https://www.linkedin.com/in/sankarraj-subramani-34254757)

> 🌛 If you like this project, star it on GitHub and share it with your QA and AI community!

