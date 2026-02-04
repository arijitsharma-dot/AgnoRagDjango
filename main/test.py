import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "main.settings"
)

django.setup()
# -----------------------------------------------
# from documents.models import Document
# from documents.utils.pdf_loader import extract_text_from_pdf
# from documents.utils.chunker import chunk_text

# doc = Document.objects.first()
# text = extract_text_from_pdf(doc.file.path)
# chunks = chunk_text(text)

# print(len(chunks))
# print(chunks[0][:200])
# -----------------------------------------------

# from documents.models import Document
# from documents.utils.pdf_loader import extract_text_from_pdf
# from documents.utils.chunker import chunk_text
# from documents.utils.embeddings import embed_texts
# from documents.utils.vector_store import add_chunks

# doc = Document.objects.first()
# text = extract_text_from_pdf(doc.file.path)
# chunks = chunk_text(text)

# embeddings = embed_texts(chunks)
# add_chunks(chunks, embeddings)

# len(chunks)
# ---------------------------------------

from documents.utils.embeddings import embed_texts
from documents.utils.vector_store import search_similar

query = "What is arijit"
query_emb = embed_texts([query])[0]

results = search_similar(query_emb)

results[0]["text"][:200]
results[0]["score"]

