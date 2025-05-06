import os
import pickle
import numpy as np
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_community.embeddings import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

# --------------------------
# CONFIGURATION
# --------------------------
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
VECTORSTORE_FILE = os.path.join(ROOT_DIR, "vectorstore.pkl")
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
EMBEDDING_CACHE_DIR = os.path.join(ROOT_DIR, "models")

# --------------------------
# LOAD VECTORSTORE
# --------------------------
try:
    with open(VECTORSTORE_FILE, "rb") as f:
        stored_embeddings, stored_documents = pickle.load(f)
except FileNotFoundError:
    raise RuntimeError(
        f"❗ vectorstore.pkl not found at {VECTORSTORE_FILE}. Please run rag_chain.py to generate it."
    )

# --------------------------
# EMBEDDING MODEL INIT
# --------------------------
embeddings_model = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL_NAME,
    cache_folder=EMBEDDING_CACHE_DIR
)

# --------------------------
# FASTAPI APP SETUP
# --------------------------
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------
# HEALTH CHECK
# --------------------------
@app.get("/")
def health_check():
    return {"message": "✅ GenQAChat backend is running!"}

# --------------------------
# ASK API ENDPOINT
# --------------------------
class QueryRequest(BaseModel):
    query: str

@app.post("/api/ask")
def ask(request: QueryRequest):
    if not request.query:
        raise HTTPException(status_code=400, detail="Query cannot be empty.")

    query_embedding = embeddings_model.embed_query(request.query)
    similarities = cosine_similarity([query_embedding], stored_embeddings)[0]
    top_index = int(np.argmax(similarities))
    top_document = stored_documents[top_index]

    return {
        "query": request.query,
        "answer": top_document.page_content.strip(),
        "similarity_score": float(similarities[top_index])
    }
