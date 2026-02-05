from documents.utils.embeddings import embed_texts
from documents.utils.vector_store import search_similar
from .rag import build_rag_prompt
from .llm import generate_answer

SIMILARITY_THRESHOLD = 0.3

def chat_with_agent(question: str) -> str:
    query_emb = embed_texts([question])[0]
    results = search_similar(query_emb)

    if results and results[0]["score"] >= SIMILARITY_THRESHOLD:
        context = "\n".join([r["text"] for r in results])
        prompt = build_rag_prompt(context, question)
        return generate_answer(prompt)

    # fallback
    return generate_answer(question)
