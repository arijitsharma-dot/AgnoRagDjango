import faiss
import pickle
import subprocess
from embeddings import EmbeddingModel

INDEX_DIR = "index"


class DocuMindRAG:
    def __init__(self):
        self.embedder = EmbeddingModel()

        self.index = faiss.read_index(f"{INDEX_DIR}/documind.index")

        with open(f"{INDEX_DIR}/texts.pkl", "rb") as f:
            self.texts = pickle.load(f)

        with open(f"{INDEX_DIR}/metadata.pkl", "rb") as f:
            self.metadata = pickle.load(f)

    def retrieve(self, query, top_k=4):
        query_vec = self.embedder.embed([query])
        distances, indices = self.index.search(query_vec, top_k)

        results = []
        for dist, idx in zip(distances[0], indices[0]):
            if dist < 1.2:  # 🔥 threshold (tunable)
                results.append({
                    "text": self.texts[idx],
                    "page": self.metadata[idx]["page"]
                })


        return results

    def generate_answer(self, query, retrieved_chunks):
        context = ""
        pages = set()

        for chunk in retrieved_chunks:
            context += f"- {chunk['text']}\n"
            pages.add(chunk["page"])

        prompt = f"""
You are DocuMind, a strict PDF-based assistant.

Answer ONLY using the context below.
If the answer is not in the context, say "I don't know."

Context:
{context}

Question:
{query}
"""

        # 🔥 WINDOWS-SAFE OLLAMA CALL
        command = "ollama run mistral"

        response = subprocess.run(
            command,
            input=prompt,
            capture_output=True,
            shell=True,
            encoding="utf-8",
            errors="ignore"
        )


        return response.stdout.strip(), sorted(pages)

