from langchain.document_loaders import TextLoader
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
import os

def seed_chromadb():
    persist_directory = "db"
    source_dir = "../knowledge_base/"
    embeddings = OpenAIEmbeddings()
    texts = []

    for filename in os.listdir(source_dir):
        loader = TextLoader(os.path.join(source_dir, filename))
        docs = loader.load()
        splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        texts.extend(splitter.split_documents(docs))

    vectordb = Chroma.from_documents(
        documents=texts,
        embedding=embeddings,
        persist_directory=persist_directory,
    )
    vectordb.persist()
    
def get_answer(question: str) -> str:
    # Basic example placeholder logic
    return f"You asked: {question} — I’ll get smarter soon!"

if __name__ == "__main__":
    seed_chromadb()
