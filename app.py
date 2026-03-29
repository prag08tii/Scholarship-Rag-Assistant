# ============================================================
# app.py  — PURE BACKEND LOGIC. NO UI CODE HERE AT ALL.
#
# This file only exposes ONE function:
#       get_answer(question)  → returns (answer, sources)
#
# It is called by:   pages/ai_chat.py
# ============================================================

import time
from rag_engine import ask_question
from semantic_cache import search_cache, store_if_liked

# Re-export store_if_liked so ai_chat.py can import it from here
# (keeps all backend imports in one place)
__all__ = ["get_answer", "store_if_liked"]


def get_answer(question: str):
    """
    Main function that ai_chat.py calls.

    Steps:
      1. Check semantic cache  → instant answer if hit
      2. If miss → run full RAG pipeline (retrieve + Groq LLM)

    Returns:
      answer  (str)  — the text answer
      sources (list) — list of source metadata dicts
      source_type (str) — "cache" or "rag"  (used for UI badge)
    """

    # STEP 1: Check cache first
    cache_result = search_cache(question)

    if cache_result:
        answer      = cache_result["answer"]
        sources     = ["⚡ From Semantic Cache"]
        source_type = "cache"
        return answer, sources, source_type

    # STEP 2: Cache miss → full RAG
    answer, sources = ask_question(question)
    source_type = "rag"

    return answer, sources, source_type