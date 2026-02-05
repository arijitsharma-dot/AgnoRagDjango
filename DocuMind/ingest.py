import os
import faiss
import pickle
from pypdf import PdfReader
from tqdm import tqdm

from embeddings import EmbeddingModel
from utils import chunk_text


PDF_PATH = "data/0000.pdf"
INDEX_DIR = "index"


def load_pdf(path):
    reader = PdfReader(path)
    pages = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            pages.append((i + 1, text))

    return pages


def main():
    os.makedirs(INDEX_DIR, exist_ok=True)

    print("📄 Loading PDF...")
    pages = load_pdf(PDF_PATH)

    texts = []
    metadata = []

    print("✂️ Chunking text...")
    for page_num, text in pages:
        chunks = chunk_text(text)
        for chunk in chunks:
            texts.append(chunk)
            metadata.append({"page": page_num})

    print(f"🔢 Total chunks: {len(texts)}")

    print("🧠 Creating embeddings...")
    embedder = EmbeddingModel()
    embeddings = embedder.embed(texts)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    faiss.write_index(index, f"{INDEX_DIR}/documind.index")

    with open(f"{INDEX_DIR}/metadata.pkl", "wb") as f:
        pickle.dump(metadata, f)

    with open(f"{INDEX_DIR}/texts.pkl", "wb") as f:
        pickle.dump(texts, f)

    print("✅ Ingestion complete. FAISS index saved.")


if __name__ == "__main__":
    main()
