import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings

# -----------------------------
# LOAD ENV
# -----------------------------
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

# -----------------------------
# EMBEDDINGS
# -----------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

SIMILARITY_THRESHOLD = 0.90


# =========================================================
# 🔍 FUNCTION 1: SEARCH CACHE
# =========================================================
def search_cache(user_question):

    embedding = embeddings.embed_query(user_question)

    with engine.connect() as conn:

        result = conn.execute(text("""
            SELECT question, answer, source,
                   1 - (embedding <=> CAST(:embedding AS vector)) AS similarity
            FROM qa_cache
            ORDER BY similarity DESC
            LIMIT 1
        """), {"embedding": embedding}).fetchone()

        if result and result.similarity and result.similarity > SIMILARITY_THRESHOLD:

            print(f"⚡ Cache HIT (similarity={result.similarity:.2f})")

            return {
                "answer": result.answer,
                "source": "cache",
                "matched_question": result.question,
                "similarity": float(result.similarity)
            }

        print("❌ Cache MISS")
        return None


# =========================================================
# ❤️ FUNCTION 2: STORE WHEN USER LIKES
# =========================================================
def store_if_liked(question, answer):

    question = question.strip()
    answer = answer.strip()

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
            print("⚠️ Already exists (Exact)")
            return False

        # -------------------------
        # 2️⃣ Semantic duplicate check
        # -------------------------
        similar = conn.execute(text("""
            SELECT 
                1 - (embedding <=> CAST(:embedding AS vector)) AS similarity
            FROM qa_cache
            ORDER BY similarity DESC
            LIMIT 1
        """), {"embedding": embedding}).fetchone()

        if similar and similar.similarity and similar.similarity > SIMILARITY_THRESHOLD:
            print(f"⚠️ Already exists (Semantic {similar.similarity:.2f})")
            return False

        # -------------------------
        # 3️⃣ Insert + initialize likes
        # -------------------------
        conn.execute(text("""
            INSERT INTO qa_cache (question, answer, embedding, source, likes)
            VALUES (:q, :a, CAST(:e AS vector), 'liked', 1)
        """), {
            "q": question,
            "a": answer,
            "e": embedding
        })

        conn.commit()

        print("✅ Stored from LIKE 👍")
        return True