from openai import OpenAI
from sentence_transformers import SentenceTransformer
from app.vector_store import index, metadata, load_store
import numpy as np

client = OpenAI(
    api_key=" ",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
) 

model = SentenceTransformer("all-MiniLM-L6-v2")

load_store()

def answer_question(question: str):
    q_embedding = model.encode([question]).astype("float32")

    D, I = index.search(q_embedding, 5)

    context = "\n".join(metadata[i]["text"] for i in I[0])

    prompt = f"""
    Use ONLY the context below to answer.

    Context:
    {context}

    Question:
    {question}
    """

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "question": question,
        "answer": response.choices[0].message.content,
        "sources": list(set(metadata[i]["source"] for i in I[0]))
    }
