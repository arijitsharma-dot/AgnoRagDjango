def build_rag_prompt(context: str, question: str) -> str:
    return f"""
Answer the question ONLY using the context below.
If the answer is not in the context, say:
"I am answering from general knowledge."

Context:
{context}

Question:
{question}
"""
