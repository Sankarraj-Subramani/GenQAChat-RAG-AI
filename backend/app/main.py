import os
import pickle
import numpy as np
from fastapi import FastAPI
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
with open(VECTORSTORE_FILE, "rb") as f:
    stored_embeddings, stored_documents = pickle.load(f)

embeddings_model = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL_NAME,
    cache_folder=EMBEDDING_CACHE_DIR
)

# --------------------------
# FASTAPI SERVER
# --------------------------
app = FastAPI()

# ✅ CORS Middleware for allowing frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to just your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------
# HEALTH CHECK ENDPOINT
# --------------------------
@app.get("/")
def root():
    return {"message": "GenQAChat backend is running"}

# --------------------------
# QUERY ENDPOINT
# --------------------------
class QueryRequest(BaseModel):
    question: str

@app.post("/query")
def query(request: QueryRequest):
    query_text = request.question
    query_embedding = embeddings_model.embed_query(query_text)

    similarities = cosine_similarity([query_embedding], stored_embeddings)[0]
    top_index = np.argmax(similarities)
    top_document = stored_documents[top_index]

    return {
        "query": query_text,
        "answer": top_document.page_content.strip(),
        "similarity_score": float(similarities[top_index])
    }
