import os
import streamlit as st
from sqlalchemy import create_engine, text
from langchain_community.embeddings import HuggingFaceEmbeddings
from groq import Groq
from dotenv import load_dotenv

# -----------------------------
# LOAD ENV VARIABLES (LOCAL)
# -----------------------------
load_dotenv()

# -----------------------------
# GET SECRETS (DEPLOYMENT / LOCAL)
# -----------------------------
DATABASE_URL = None
GROQ_API_KEY = None

# Try Streamlit secrets first
try:
    DATABASE_URL = st.secrets["DATABASE_URL"]
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except Exception:
    # fallback to .env
    DATABASE_URL = os.getenv("DATABASE_URL")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Safety check
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set")

# -----------------------------
# DATABASE CONNECTION
# -----------------------------
engine = create_engine(DATABASE_URL)

# -----------------------------
# EMBEDDING MODEL
# -----------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

# -----------------------------
# GROQ CLIENT
# -----------------------------
client = Groq(api_key=GROQ_API_KEY)

# -----------------------------
# RETRIEVE CHUNKS FROM DATABASE
# -----------------------------
def retrieve_chunks(question):

    query_vector = embeddings.embed_query(question)
    query_vector = str(query_vector)

    sql = text("""
        SELECT document, cmetadata
        FROM langchain_pg_embedding
        ORDER BY embedding <-> :query_vector
        LIMIT 4
    """)

    with engine.connect() as conn:
        results = conn.execute(sql, {"query_vector": query_vector}).fetchall()

    chunks = []
    sources = []

    for row in results:
        document = row[0]
        metadata = row[1]

        chunks.append(document)
        sources.append(metadata)

    return chunks, sources


# -----------------------------
# RAG QUESTION ANSWERING
# -----------------------------
def ask_question(question):

    chunks, sources = retrieve_chunks(question)

    context = "\n\n".join(chunks)

    prompt = f"""
You are an AI assistant helping Indian students find scholarship information.

Rules:
- Use ONLY the provided context
- Do NOT add outside knowledge
- If information is missing say:
"I couldn't find this information in the scholarship guidelines."

Formatting Rules:
- Always answer in a structured format
- Use bullet points or numbered lists
- Do NOT write long paragraphs
- Keep answers clear and easy to read."

---------------------
Context:
{context}
---------------------

Question: {question}

Answer clearly for students.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    answer = response.choices[0].message.content

    return answer, sources
