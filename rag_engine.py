import os
from sqlalchemy import create_engine, text
from langchain_community.embeddings import HuggingFaceEmbeddings
from groq import Groq
from dotenv import load_dotenv

# -----------------------------
# LOAD ENV VARIABLES
# -----------------------------
load_dotenv()

# -----------------------------
# DATABASE CONNECTION
# -----------------------------
DATABASE_URL = os.getenv("DATABASE_URL")

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
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

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
You are a helpful assistant answering student scholarship questions.

Use ONLY the information from the context below.

If the answer is not present in the context, say:
"I couldn't find this information in the scholarship guidelines."

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