import streamlit as st
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
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
EMBEDDING_CACHE_DIR = os.path.join(ROOT_DIR, "models")

# --------------------------
# LOAD VECTORSTORE
# --------------------------
@st.cache_resource
def load_vectorstore():
    try:
        with open(VECTORSTORE_FILE, "rb") as f:
            stored_embeddings, stored_documents = pickle.load(f)
        embeddings_model = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL_NAME,
            cache_folder=EMBEDDING_CACHE_DIR
        )
        return stored_embeddings, stored_documents, embeddings_model
    except FileNotFoundError:
        st.error("❗ vectorstore.pkl not found. Please run rag_chain.py to generate it.")
        st.stop()

stored_embeddings, stored_documents, embeddings_model = load_vectorstore()

# --------------------------
# STREAMLIT UI
# --------------------------
st.set_page_config(page_title="GenQAChat", page_icon="🤖")
st.title("🤖 GenQAChat - Streamlit Edition")
st.markdown("Ask any QA automation question and get an AI-powered answer from your local knowledge base.")

query = st.text_input("🔍 Enter your question below:")

if st.button("Ask") and query:
    query_embedding = embeddings_model.embed_query(query)
    similarities = cosine_similarity([query_embedding], stored_embeddings)[0]
    top_index = int(np.argmax(similarities))
    top_document = stored_documents[top_index]

    st.success("✅ Best Match Found:")
    st.markdown(top_document.page_content.strip())
    st.caption(f"🔗 Similarity Score: {similarities[top_index]:.4f}")