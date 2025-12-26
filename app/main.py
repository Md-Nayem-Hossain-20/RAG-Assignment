from fastapi import FastAPI, UploadFile, File
from app.ingest import process_document
from app.query import answer_question

app = FastAPI(title="RAG Document QA API")

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    return process_document(file)

@app.post("/query")
async def query(question: str):
    return answer_question(question)
