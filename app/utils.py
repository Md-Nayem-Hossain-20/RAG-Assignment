import pdfplumber
from docx import Document
from PIL import Image
import pytesseract
import pandas as pd

def extract_text(path: str) -> str:
    if path.endswith(".pdf"):
        with pdfplumber.open(path) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages)

    if path.endswith(".docx"):
        doc = Document(path)
        return "\n".join(p.text for p in doc.paragraphs)

    if path.endswith(".txt"):
        return open(path, "r", encoding="utf-8").read()

    if path.endswith((".jpg", ".png")):
        return pytesseract.image_to_string(Image.open(path))

    if path.endswith(".csv"):
        return pd.read_csv(path).to_string()

    raise ValueError("Unsupported file type")
