# 📄 RAG-based Document Question Answering System

This project is a **Retrieval-Augmented Generation (RAG)** based Document Question Answering system built using **FastAPI**, **LangChain**, and **Streamlit**.

Users can:
- Upload documents (PDF / TXT / CSV / DOCX / Images)
- Ask questions based on the uploaded content
- Receive AI-generated answers grounded in the document text

The system uses embeddings + vector search to retrieve relevant document chunks before generating answers.

---

## 🧠 Project Architecture (High Level)

```
User
│
│ Upload / Ask Question
▼
Streamlit Frontend
│
│ REST API calls
▼
FastAPI Backend
│
├── Document Ingestion
│ ├── Text Extraction (PDF / Image / Text)
│ ├── Text Splitting
│ ├── Embedding Generation
│ └── Vector Store (FAISS)
│
└── Question Answering
├── Similarity Search
└── LLM Response Generation

```

---

## 🛠 Tech Stack

- **Python 3.12.10**
- **FastAPI** – Backend API
- **Streamlit** – Frontend UI
- **LangChain** – RAG pipeline
- **FAISS** – Vector database
- **Sentence Transformers / OpenAI Embeddings**
- **langchain_text_splitters** - Break and Chunk text
- **Pdfplumber** – PDF text extraction
- **Pillow + pytesseract** – OCR for images
- **Uvicorn** – ASGI server

---

## 🚀 Installation Guide (From Scratch)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/rag_assign.git
cd rag_assign
```

###### Install **UV**  and then add it. You can also use Python **Virtualenv**.
```bash
uv init
```
```bash
uv venv
```
```bash
.venv\Scripts\activate # On Windows
source .venv/bin/activate # On Linux/Mac Os

```
###### Using Python Virtualenv
```bash
python -m venv venv
source venv/bin/activate  # On Windows: `venv\Scripts\activate`
```

### 3️⃣ Install Dependencies

```bash
uv pip install -r requirements.txt
```

### 4️⃣ Install Tesseract OCR (for Image Processing)

If you plan to process image files (PNG, JPG, etc.), you need to install Tesseract OCR on your system.

- **Windows:** Download and install from [Tesseract-OCR GitHub](https://tesseract-ocr.github.io/tessdoc/Installation.html). Make sure to add Tesseract to your system's PATH.
- **macOS:** `brew install tesseract`
- **Linux (Debian/Ubuntu):** `sudo apt update && sudo apt install tesseract-ocr`

## Optional But Important

#### I'm using geminiAPI key bcz it's free and I can run through *OPENAI Library*  using *OpenAI compatibility with GeminiAPI*
#### Before run this project you must provide Google GeminiAPI key at *app/query.py* file. 

#### If you want to use *OpenAI API* you also can by adding *.env* file at *app* folder. In *.env* file add your *OpenAI API Key*

### 5️⃣ Run the FastAPI Backend

```bash
uv run uvicorn app.main:app --reload
```

The backend API will be accessible at `http://localhost:8000`.

### 6️⃣ Run the Streamlit Frontend

Open a new terminal, navigate to the project directory, and run:

```bash
uv run streamlit run frontend/streamlit_app.py
```

The Streamlit app will be accessible at `http://localhost:8501`.


## ⚠️ Important Notes

- /upload and /query only accept POST requests

- 405 Method Not Allowed for GET requests is expected behavior

- OCR requires Tesseract installed

- FAISS vector store is in-memory

- Restarting the backend clears stored embeddings
