import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

VECTOR_STORE = []

def add_chunks(chunks, embeddings):
    for text, emb in zip(chunks, embeddings):
        VECTOR_STORE.append({
            "text": text,
            "embedding": emb
        })

def search_similar(query_embedding, top_k=3):
    if not VECTOR_STORE:
        return []

    vectors = [item["embedding"] for item in VECTOR_STORE]
    similarities = cosine_similarity(
        [query_embedding], vectors
    )[0]

    top_indices = similarities.argsort()[-top_k:][::-1]

    return [
        {
            "text": VECTOR_STORE[i]["text"],
            "score": similarities[i]
        }
        for i in top_indices
    ]
