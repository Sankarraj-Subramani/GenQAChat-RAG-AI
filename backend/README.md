# GenQAChat Backend

This is the **FastAPI** backend server for the `GenQAChat` project — an AI-powered QA knowledge base chatbot that uses:

- FastAPI (Python server)
- HuggingFace Embeddings (for text encoding)
- FAISS/ChromaDB (vector storage)
- LangChain integration
- OpenAI (optional for enhancements)

## 🚀 How it Works

- Loads curated `.md` knowledge files.
- Splits and embeds documents using HuggingFace Sentence Transformers.
- Stores the embeddings using FAISS (or optionally ChromaDB).
- Exposes an API endpoint (`/query`) for answering user questions based on semantic search.


## 📂 Project Structure

```bash
backend/
  ├── app/
  │   ├── main.py        # FastAPI server (entry point)
  │   └── rag_chain.py   # Vectorstore generation from markdown files
  └── requirements.txt  # Backend dependencies
knowledge_base/
  └── *.md        # Markdown knowledge files
vectorstore.pkl         # Saved vector database (FAISS serialized)
models/                 # Cached HuggingFace models
```

## 🔧 Setup Instructions

1. **Create a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

2. **Install dependencies**

```bash
pip install -r backend/requirements.txt
```

3. **Generate Vectorstore**

```bash
cd backend/app
python rag_chain.py
```

✅ This will create `vectorstore.pkl` using all `.md` files from `knowledge_base/`.

4. **Start the FastAPI server**

```bash
cd backend
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Your backend will now run at:
```
http://localhost:8000
```

API Swagger docs:
```
http://localhost:8000/docs
```


## 📬 API Endpoint

- `POST /query`
- Body:

```json
{
  "question": "What is Selenium?"
}
```

- Response:

```json
{
  "query": "What is Selenium?",
  "answer": "Selenium is an open-source framework for automating web applications...",
  "similarity_score": 0.92
}
```


## 📚 Tech Stack

- **FastAPI** — Python web server
- **HuggingFace Sentence Transformers** — Embedding model
- **FAISS/ChromaDB** — Vector similarity search
- **LangChain** — Abstractions and document processing
- **OpenAI (optional)** — GPT-based enhancements (coming soon)


## ✨ Credits

Developed by **Sankarraj Subramani** as part of the EB2-NIW/EB1A profile enhancement journey.

---

> Ready to scale by adding more `.md` knowledge files 🚀!
