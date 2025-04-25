import nltk
nltk.download('punkt')

import os
import pickle
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# --------------------------
# CONFIGURATION
# --------------------------
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA_DIR = os.path.join(ROOT_DIR, "knowledge_base")
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
EMBEDDING_CACHE_DIR = os.path.join(ROOT_DIR, "models")
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
VECTORSTORE_FILE = os.path.join(ROOT_DIR, "vectorstore.pkl")

# --------------------------
# LOAD AND SPLIT DOCUMENTS
# --------------------------
def load_and_split_documents():
    loader = DirectoryLoader(
        path=DATA_DIR,
        glob="**/*.md",  # Change to "*.txt" if needed
        loader_cls=UnstructuredMarkdownLoader,
        show_progress=True
    )
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    return splitter.split_documents(documents)

# --------------------------
# EMBED DOCUMENTS
# --------------------------
def embed_documents(documents, embeddings_model):
    texts = [doc.page_content for doc in documents]
    embeddings = embeddings_model.embed_documents(texts)
    return embeddings

# --------------------------
# SAVE VECTORSTORE
# --------------------------
def save_vectorstore(embeddings, documents):
    with open(VECTORSTORE_FILE, "wb") as f:
        pickle.dump((embeddings, documents), f)
    print(f"✅ Vectorstore saved at {VECTORSTORE_FILE}")

# --------------------------
# MAIN
# --------------------------
if __name__ == "__main__":
    print("🔄 Loading documents and generating embeddings...")

    documents = load_and_split_documents()
    embeddings_model = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME,
        cache_folder=EMBEDDING_CACHE_DIR
    )
    embeddings = embed_documents(documents, embeddings_model)

    save_vectorstore(embeddings, documents)
