import streamlit as st

def render():
    st.markdown("""
<style>
.arch-wrap{max-width:860px;margin:0 auto;padding:5rem 2rem;margin-top:68px}
.sec-eyebrow{font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);margin-bottom:1rem;display:block}
.sec-title{font-family:var(--font-display);font-size:clamp(2rem,5vw,3.5rem);font-weight:300;color:var(--text);line-height:1.1;margin-bottom:2.5rem}
.sec-title em{font-style:italic;color:var(--gold2)}
.pipeline-stage{background:var(--card);border:.5px solid var(--border);border-radius:12px;padding:1.5rem 2rem;margin-bottom:0}
.stage-label{font-size:.72rem;letter-spacing:.15em;text-transform:uppercase;color:var(--gold);margin-bottom:1rem;display:flex;align-items:center;gap:.75rem}
.stage-num{width:24px;height:24px;border-radius:50%;background:var(--goldF);border:.5px solid var(--border2);color:var(--gold2);font-size:.78rem;display:flex;align-items:center;justify-content:center;flex-shrink:0;font-family:var(--font-display)}
.stage-nodes{display:flex;gap:1rem;flex-wrap:wrap}
.node{flex:1;min-width:140px;padding:1rem;border-radius:8px;border:.5px solid transparent}
.node.blue{background:rgba(79,142,247,.07);border-color:rgba(79,142,247,.2)}
.node.green{background:rgba(52,211,153,.07);border-color:rgba(52,211,153,.2)}
.node.teal{background:rgba(45,212,191,.07);border-color:rgba(45,212,191,.2)}
.node.rose{background:rgba(244,114,182,.07);border-color:rgba(244,114,182,.2)}
.node-ico{font-size:1.3rem;margin-bottom:.4rem}
.node-name{font-size:.85rem;font-weight:500;color:var(--text)}
.node-desc{font-size:.75rem;color:var(--muted);margin-top:.25rem}
.stage-arrow{text-align:center;color:var(--border2);font-size:1.5rem;padding:.4rem 0}
.tech-eyebrow{font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);margin-bottom:1rem;display:block;margin-top:3rem}
.tech-row{display:flex;flex-wrap:wrap;gap:1rem;margin-top:.5rem}
.tech-item{display:flex;align-items:center;gap:.75rem;background:var(--card);border:.5px solid var(--border);border-radius:8px;padding:.85rem 1.25rem;flex:1;min-width:160px}
.tech-ico{font-size:1.5rem}
.tech-name{font-size:.88rem;font-weight:500;color:var(--text)}
.tech-role{font-size:.75rem;color:var(--muted)}
</style>

<div class="arch-wrap">
  <span class="sec-eyebrow">Under the Hood</span>
  <div class="sec-title">The RAG <em>Pipeline</em></div>

  <div class="pipeline-stage">
    <div class="stage-label"><span class="stage-num">1</span> Document Ingestion</div>
    <div class="stage-nodes">
      <div class="node blue"><div class="node-ico">&#128193;</div><div class="node-name">PDF Loader</div><div class="node-desc">PyPDFLoader reads all PDFs</div></div>
      <div class="node blue"><div class="node-ico">&#9988;&#65039;</div><div class="node-name">Text Splitter</div><div class="node-desc">Chunks with overlap</div></div>
      <div class="node blue"><div class="node-ico">&#127991;&#65039;</div><div class="node-name">Metadata</div><div class="node-desc">Source file + scheme tag</div></div>
    </div>
  </div>
  <div class="stage-arrow">&#8595;</div>

  <div class="pipeline-stage">
    <div class="stage-label"><span class="stage-num">2</span> Embedding &amp; Storage</div>
    <div class="stage-nodes">
      <div class="node teal"><div class="node-ico">&#129504;</div><div class="node-name">HuggingFace Embeddings</div><div class="node-desc">paraphrase-multilingual-MiniLM</div></div>
      <div class="node teal"><div class="node-ico">&#128447;&#65039;</div><div class="node-name">Supabase pgvector</div><div class="node-desc">Vector storage</div></div>
      <div class="node teal"><div class="node-ico">&#9889;</div><div class="node-name">Semantic Cache</div><div class="node-desc">qa_cache table, 0.90 threshold</div></div>
    </div>
  </div>
  <div class="stage-arrow">&#8595;</div>

  <div class="pipeline-stage">
    <div class="stage-label"><span class="stage-num">3</span> Query &amp; Retrieval</div>
    <div class="stage-nodes">
      <div class="node green"><div class="node-ico">&#128172;</div><div class="node-name">User Query</div><div class="node-desc">Natural language input</div></div>
      <div class="node teal"><div class="node-ico">&#128270;</div><div class="node-name">Cache Check</div><div class="node-desc">Instant if similarity &gt; 0.90</div></div>
      <div class="node green"><div class="node-ico">&#128225;</div><div class="node-name">Top-4 Retrieval</div><div class="node-desc">pgvector similarity search</div></div>
    </div>
  </div>
  <div class="stage-arrow">&#8595;</div>

  <div class="pipeline-stage">
    <div class="stage-label"><span class="stage-num">4</span> Generation &amp; Feedback</div>
    <div class="stage-nodes">
      <div class="node rose"><div class="node-ico">&#129302;</div><div class="node-name">Groq LLM</div><div class="node-desc">llama-3.1-8b-instant</div></div>
      <div class="node rose"><div class="node-ico">&#128206;</div><div class="node-name">Source Citations</div><div class="node-desc">PDF provenance metadata</div></div>
      <div class="node rose"><div class="node-ico">&#128077;</div><div class="node-name">Feedback Loop</div><div class="node-desc">Like &#8594; stored to qa_cache</div></div>
    </div>
  </div>

  <span class="tech-eyebrow">Tech Stack</span>
  <div class="tech-row">
    <div class="tech-item"><div class="tech-ico">&#129988;</div><div><div class="tech-name">LangChain</div><div class="tech-role">RAG orchestration</div></div></div>
    <div class="tech-item"><div class="tech-ico">&#128447;&#65039;</div><div><div class="tech-name">Supabase</div><div class="tech-role">Vector DB (pgvector)</div></div></div>
    <div class="tech-item"><div class="tech-ico">&#9889;</div><div><div class="tech-name">Semantic Cache</div><div class="tech-role">Fast repeat queries</div></div></div>
    <div class="tech-item"><div class="tech-ico">&#129302;</div><div><div class="tech-name">Groq</div><div class="tech-role">llama-3.1-8b-instant</div></div></div>
    <div class="tech-item"><div class="tech-ico">&#128013;</div><div><div class="tech-name">Python</div><div class="tech-role">Backend engine</div></div></div>
    <div class="tech-item"><div class="tech-ico">&#129303;</div><div><div class="tech-name">HuggingFace</div><div class="tech-role">Multilingual embeddings</div></div></div>
  </div>
</div>
""", unsafe_allow_html=True)