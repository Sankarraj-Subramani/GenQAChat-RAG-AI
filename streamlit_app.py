# This patch prevents torch class registration errors on some environments (optional)
import sys
if 'torch' in sys.modules:
    import types
    sys.modules['torch'].classes = types.SimpleNamespace(_path=[])

import streamlit as st
st.set_page_config(page_title="GenQAChat", page_icon="🤖", layout="centered")

import pickle
import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from langchain_community.embeddings import HuggingFaceEmbeddings

# Configuration
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
VECTORSTORE_FILE = os.path.join(ROOT_DIR, "vectorstore.pkl")
EMBEDDING_MODEL_PATH = os.path.join(ROOT_DIR, "models", "all-MiniLM-L6-v2")
SAFE_FALLBACK_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

@st.cache_resource(show_spinner="🔄 Loading local embeddings and vectorstore...")
def load_vectorstore():
    if not os.path.exists(VECTORSTORE_FILE):
        st.error("❗ `vectorstore.pkl` not found. Please run `backend/app/rag_chain.py` to generate it.")
        st.stop()

    # Load stored embeddings and documents
    with open(VECTORSTORE_FILE, "rb") as f:
        stored_embeddings, stored_documents = pickle.load(f)

    try:
        # Try loading local model (may break if config has 'include_prompt')
        embeddings_model = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL_PATH,
            cache_folder=EMBEDDING_MODEL_PATH
        )
    except TypeError as e:
        st.warning(f"⚠️ Local model may be incompatible: {e}. Falling back to safe online model.")
        embeddings_model = HuggingFaceEmbeddings(model_name=SAFE_FALLBACK_MODEL)

    return stored_embeddings, stored_documents, embeddings_model

# Load everything
stored_embeddings, stored_documents, embeddings_model = load_vectorstore()

# Streamlit UI
st.title("🤖 GenQAChat – AI QA Assistant")
st.markdown("Ask your **QA automation** question below and get a trusted answer powered by LangChain + local embeddings.")

with st.form("ask_form"):
    query = st.text_input("🔍 Your Question:")
    submit = st.form_submit_button("Ask")

if submit and query:
    with st.spinner("🔎 Searching for best match..."):
        query_embedding = embeddings_model.embed_query(query)
        similarities = cosine_similarity([query_embedding], stored_embeddings)[0]
        top_index = int(np.argmax(similarities))
        top_document = stored_documents[top_index]

        st.success("✅ Best Match Found:")
        st.markdown(top_document.page_content.strip())
        st.caption(f"📈 Similarity Score: {similarities[top_index]:.4f}")

st.markdown("---")
st.caption("GenQAChat © 2025 • Built with FastAPI, LangChain, HuggingFace, and Streamlit.")
