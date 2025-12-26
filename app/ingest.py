import os, uuid, shutil
from fastapi import UploadFile
from app.utils import extract_text
from app.embeddings import chunk_text, embed_chunks
from app.vector_store import save_embeddings

UPLOAD_DIR = "data/uploads"

def process_document(file: UploadFile):
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_id = str(uuid.uuid4())
    file_path = f"{UPLOAD_DIR}/{file_id}_{file.filename}"

    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    text = extract_text(file_path)
    chunks = chunk_text(text)
    embeddings = embed_chunks(chunks)

    save_embeddings(embeddings, chunks, file.filename)

    return {
        "file_id": file_id,
        "filename": file.filename,
        "chunks": len(chunks)
    }
