import streamlit as st
st.set_page_config(page_title="GenQAChat", page_icon="🤖", layout="centered")

import pickle
import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from langchain_community.embeddings import HuggingFaceEmbeddings

# --------------------------
# CONFIGURATION
# --------------------------
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
VECTORSTORE_FILE = os.path.join(ROOT_DIR, "vectorstore.pkl")
EMBEDDING_MODEL_PATH = os.path.join(ROOT_DIR, "models", "all-MiniLM-L6-v2")

# --------------------------
# LOAD VECTORSTORE + EMBEDDINGS
# --------------------------
@st.cache_resource(show_spinner="🔄 Loading local embeddings and vectorstore...")
def load_vectorstore():
    if not os.path.exists(VECTORSTORE_FILE):
        st.error("❗ vectorstore.pkl not found. Please run `backend/app/rag_chain.py` to generate it.")
        st.stop()

    if not os.path.exists(EMBEDDING_MODEL_PATH):
        st.error("❗ Local model not found. Please run the model download script to populate ./models/all-MiniLM-L6-v2")
        st.stop()

    with open(VECTORSTORE_FILE, "rb") as f:
        stored_embeddings, stored_documents = pickle.load(f)

    embeddings_model = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_PATH,
        cache_folder=EMBEDDING_MODEL_PATH
    )

    return stored_embeddings, stored_documents, embeddings_model

stored_embeddings, stored_documents, embeddings_model = load_vectorstore()

# --------------------------
# STREAMLIT UI
# --------------------------
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
