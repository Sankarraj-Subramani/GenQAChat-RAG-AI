
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.rag_chain import get_answer

app = FastAPI()

# CORS settings - allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For local/Codespaces use only – secure this for prod!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for request body
class Question(BaseModel):
    question: str

# Route to handle chat question
@app.post("/ask")
async def ask_question(query: Question):
    answer = get_answer(query.question)
    return {"answer": answer}



@app.get("/")
def read_root():
    return {"message": "GenQAChat backend is running!"}
