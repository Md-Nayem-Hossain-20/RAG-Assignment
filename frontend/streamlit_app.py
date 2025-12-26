import streamlit as st
import requests
import os

API_URL = os.getenv("API_URL", "http://localhost:8000")

st.set_page_config(page_title="RAG Document QA")

st.title("📄 Your Personal Chatbot for Question Answering")

st.header("📤 Upload Document")

file = st.file_uploader(
    "Upload PDF, DOCX, TXT, CSV, JPG, PNG",
    type=["pdf", "docx", "txt", "csv", "jpg", "png"]
)

if file:
    with st.spinner("Uploading..."):
        res = requests.post(
            f"{API_URL}/upload",
            files={"file": (file.name, file, file.type)}
        )
    if res.status_code == 200:
        st.success("Upload successful")
        st.json(res.json())
    else:
        st.error("Upload failed")

st.header("❓ Ask a Question")

question = st.text_input("Your question")

if st.button("Get Answer") and question:
    with st.spinner("Thinking..."):
        res = requests.post(
            f"{API_URL}/query",
            params={"question": question}
        )
    if res.status_code == 200:
        data = res.json()
        st.subheader("Answer")
        st.write(data["answer"])

        st.subheader("Sources")
        for src in data["sources"]:
            st.write("-", src)
    else:
        st.error("Failed to get answer")
