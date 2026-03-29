# ============================================================
# pages/architecture.py
# PURPOSE : RAG pipeline diagram + tech stack
# Used by : main.py  →  when ?page=architecture
# ============================================================

import streamlit as st

def render():
    """Renders the Architecture / How It Works page."""

    st.markdown("""
    <div class="section-wrap">
      <span class="sec-eyebrow">Under the Hood</span>
      <div class="sec-title">The RAG <em>Pipeline</em></div>

      <!-- Stage 1 -->
      <div class="pipeline-stage">
        <div class="stage-label" data-n="1">Document Ingestion</div>
        <div class="stage-nodes">
          <div class="node blue"><div class="node-ico">📁</div><div class="node-name">PDF Loader</div><div class="node-desc">PyPDFLoader reads all PDFs</div></div>
          <div class="node blue"><div class="node-ico">✂️</div><div class="node-name">Text Splitter</div><div class="node-desc">Chunks with overlap</div></div>
          <div class="node blue"><div class="node-ico">🏷️</div><div class="node-name">Metadata</div><div class="node-desc">Source file + scheme tag</div></div>
        </div>
      </div>
      <div class="stage-arrow">↓</div>

      <!-- Stage 2 -->
      <div class="pipeline-stage">
        <div class="stage-label" data-n="2">Embedding &amp; Storage</div>
        <div class="stage-nodes">
          <div class="node teal"><div class="node-ico">🧠</div><div class="node-name">HuggingFace Embeddings</div><div class="node-desc">paraphrase-multilingual-MiniLM</div></div>
          <div class="node teal"><div class="node-ico">🗄️</div><div class="node-name">Supabase pgvector</div><div class="node-desc">Vector storage</div></div>
          <div class="node teal"><div class="node-ico">⚡</div><div class="node-name">Semantic Cache</div><div class="node-desc">qa_cache table, 0.90 threshold</div></div>
        </div>
      </div>
      <div class="stage-arrow">↓</div>

      <!-- Stage 3 -->
      <div class="pipeline-stage">
        <div class="stage-label" data-n="3">Query &amp; Retrieval</div>
        <div class="stage-nodes">
          <div class="node green"><div class="node-ico">💬</div><div class="node-name">User Query</div><div class="node-desc">Natural language input</div></div>
          <div class="node teal"><div class="node-ico">🔎</div><div class="node-name">Cache Check</div><div class="node-desc">Instant if similarity &gt; 0.90</div></div>
          <div class="node green"><div class="node-ico">📡</div><div class="node-name">Top-4 Retrieval</div><div class="node-desc">pgvector similarity search</div></div>
        </div>
      </div>
      <div class="stage-arrow">↓</div>

      <!-- Stage 4 -->
      <div class="pipeline-stage">
        <div class="stage-label" data-n="4">Generation &amp; Feedback</div>
        <div class="stage-nodes">
          <div class="node rose"><div class="node-ico">🤖</div><div class="node-name">Groq LLM</div><div class="node-desc">llama-3.1-8b-instant</div></div>
          <div class="node rose"><div class="node-ico">📎</div><div class="node-name">Source Citations</div><div class="node-desc">PDF provenance metadata</div></div>
          <div class="node rose"><div class="node-ico">👍</div><div class="node-name">Feedback Loop</div><div class="node-desc">Like → stored to qa_cache</div></div>
        </div>
      </div>

      <!-- Tech Stack -->
      <div style="margin-top:3.5rem;">
        <span class="sec-eyebrow">Tech Stack</span>
        <div class="tech-row">
          <div class="tech-item"><div class="tech-ico">🦜</div><div><div class="tech-name">LangChain</div><div class="tech-role">RAG orchestration</div></div></div>
          <div class="tech-item"><div class="tech-ico">🗄️</div><div><div class="tech-name">Supabase</div><div class="tech-role">Vector DB (pgvector)</div></div></div>
          <div class="tech-item"><div class="tech-ico">⚡</div><div><div class="tech-name">Semantic Cache</div><div class="tech-role">Fast repeat queries</div></div></div>
          <div class="tech-item"><div class="tech-ico">🤖</div><div><div class="tech-name">Groq</div><div class="tech-role">llama-3.1-8b-instant</div></div></div>
          <div class="tech-item"><div class="tech-ico">🐍</div><div><div class="tech-name">Python</div><div class="tech-role">Backend engine</div></div></div>
          <div class="tech-item"><div class="tech-ico">🤗</div><div><div class="tech-name">HuggingFace</div><div class="tech-role">Multilingual embeddings</div></div></div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)