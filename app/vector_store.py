import faiss, os, pickle
import numpy as np

INDEX_PATH = "data/faiss_index/index.bin"
META_PATH = "data/faiss_index/meta.pkl"

dimension = 384
index = faiss.IndexFlatL2(dimension)
metadata = []

def save_embeddings(embeddings, chunks, filename):
    global metadata

    os.makedirs("data/faiss_index", exist_ok=True)

    index.add(np.array(embeddings).astype("float32"))

    for chunk in chunks:
        metadata.append({
            "text": chunk,
            "source": filename
        })

    faiss.write_index(index, INDEX_PATH)
    pickle.dump(metadata, open(META_PATH, "wb"))

def load_store():
    global index, metadata
    if os.path.exists(INDEX_PATH):
        index = faiss.read_index(INDEX_PATH)
        metadata = pickle.load(open(META_PATH, "rb"))
