import json
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings

# -----------------------------
# LOAD ENV VARIABLES
# -----------------------------
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

# -----------------------------
# EMBEDDING MODEL
# -----------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

SIMILARITY_THRESHOLD = 0.90


# -----------------------------
# FUNCTION: STORE ONE Q&A
# -----------------------------
def store_qa(question, answer, source="manual"):

    question = question.strip()
    answer = answer.strip()

    # 🔹 Create embedding
    embedding = embeddings.embed_query(question)

    with engine.connect() as conn:

        # -------------------------
        # 1️⃣ Exact duplicate check
        # -------------------------
        exact = conn.execute(text("""
            SELECT 1 FROM qa_cache
            WHERE LOWER(question) = LOWER(:q)
        """), {"q": question}).fetchone()

        if exact:
            print("⚠️ Already exists in table (Exact match)")
            return

        # -------------------------
        # 2️⃣ Semantic duplicate check (FIXED)
        # -------------------------
        similar = conn.execute(text("""
            SELECT 
                1 - (embedding <=> CAST(:embedding AS vector)) AS similarity
            FROM qa_cache
            ORDER BY similarity DESC
            LIMIT 1
        """), {"embedding": embedding}).fetchone()

        if similar and similar.similarity and similar.similarity > SIMILARITY_THRESHOLD:
            print(f"⚠️ Already exists (Semantic match: {similar.similarity:.2f})")
            return

        # -------------------------
        # 3️⃣ Insert into DB (FIXED)
        # -------------------------
        conn.execute(text("""
            INSERT INTO qa_cache (question, answer, embedding, source)
            VALUES (:q, :a, CAST(:e AS vector), :s)
        """), {
            "q": question,
            "a": answer,
            "e": embedding,
            "s": source
        })

        conn.commit()

        print("✅ Stored successfully!")


# -----------------------------
# FUNCTION: BULK INSERT FROM JSON
# -----------------------------
def load_json_and_store(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        print(f"\n🔍 Processing: {item['question']}")
        store_qa(
            question=item["question"],
            answer=item["answer"],
            source="manual"
        )


# -----------------------------
# RUN SCRIPT
# -----------------------------
if __name__ == "__main__":
    load_json_and_store("qa_data.json")