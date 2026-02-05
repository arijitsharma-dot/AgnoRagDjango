from transformers import pipeline

llm = pipeline(
    task="text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=256
)

def generate_answer(prompt: str) -> str:
    result = llm(prompt)
    return result[0]["generated_text"]
