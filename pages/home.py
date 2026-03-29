import streamlit as st

def render():
    st.markdown("""
<style>
.sp-hero{min-height:calc(100vh - 68px);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:5rem 1.5rem 4rem;margin-top:68px;position:relative;overflow:hidden}
.sp-hero::before{content:'';position:absolute;top:50%;left:50%;transform:translate(-50%,-60%);width:900px;height:600px;background:radial-gradient(ellipse,rgba(201,168,76,.07) 0%,transparent 65%);pointer-events:none}
.hero-eyebrow{display:inline-flex;align-items:center;gap:.75rem;font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);border:.5px solid var(--border2);border-radius:999px;padding:.4rem 1.25rem;margin-bottom:2.25rem}
.hline{width:20px;height:.5px;background:var(--gold);opacity:.5;display:inline-block}
.sp-h1{font-family:var(--font-display);font-size:clamp(3.2rem,7vw,6.5rem);font-weight:300;line-height:1.05;color:#fff;margin-bottom:.5rem}
.sp-h1 strong{font-weight:600;font-style:italic;background:linear-gradient(135deg,var(--gold2),var(--gold3));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.sp-h1 .line2{color:rgba(255,255,255,.45);font-weight:300;display:block}
.hero-desc{max-width:520px;margin:2rem auto 3rem;font-size:1rem;font-weight:300;color:var(--muted2);line-height:1.8}
.hero-actions{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap}
.btn-gold{background:var(--gold);color:#060810;border:none;padding:.85rem 2.25rem;border-radius:8px;font-family:var(--font-body);font-size:.88rem;font-weight:600;letter-spacing:.04em;cursor:pointer;text-transform:uppercase;text-decoration:none;transition:background .2s,transform .15s;display:inline-block}
.btn-gold:hover{background:var(--gold2);transform:translateY(-2px);color:#000}
.btn-ghost{background:transparent;color:var(--gold);border:.5px solid var(--border2);padding:.85rem 2.25rem;border-radius:8px;font-family:var(--font-body);font-size:.88rem;letter-spacing:.04em;cursor:pointer;text-transform:uppercase;text-decoration:none;transition:border-color .2s,color .2s;display:inline-block}
.btn-ghost:hover{border-color:var(--gold2);color:var(--gold2)}
.stats-row{display:flex;gap:2px;justify-content:center;margin-top:5rem;flex-wrap:wrap}
.stat-card{background:var(--card);border:.5px solid var(--border);padding:1.75rem 2.5rem;text-align:center;flex:1;min-width:150px}
.stat-card:first-child{border-radius:12px 0 0 12px}
.stat-card:last-child{border-radius:0 12px 12px 0}
.stat-n{font-family:var(--font-display);font-size:2.4rem;font-weight:600;color:var(--gold2);line-height:1}
.stat-l{font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-top:.5rem}
.section-wrap{max-width:900px;margin:0 auto;padding:5rem 2rem}
.sec-eyebrow{font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);margin-bottom:1rem;display:block}
.sec-title{font-family:var(--font-display);font-size:clamp(2rem,5vw,3.5rem);font-weight:300;color:#fff;line-height:1.1;margin-bottom:1.5rem}
.sec-title em{font-style:italic;color:var(--gold2)}
.problem-intro{font-size:1.05rem;color:var(--muted2);line-height:1.85;max-width:680px;margin-bottom:2.5rem}
.problem-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:1.25rem;margin-bottom:2.5rem}
.problem-card{background:linear-gradient(135deg,rgba(244,114,182,.05),var(--card));border:.5px solid rgba(244,114,182,.15);border-radius:14px;padding:1.75rem;transition:transform .2s,border-color .2s}
.problem-card:hover{transform:translateY(-3px);border-color:rgba(244,114,182,.3)}
.problem-icon{font-size:2rem;margin-bottom:.75rem}
.problem-tag{font-size:.68rem;letter-spacing:.15em;text-transform:uppercase;color:var(--rose);margin-bottom:.4rem}
.problem-title{font-family:var(--font-display);font-size:1.15rem;font-weight:600;color:#fff;margin-bottom:.6rem}
.problem-desc{font-size:.87rem;color:var(--muted2);line-height:1.75}
.psb{background:var(--card);border:.5px solid var(--border);border-radius:14px;padding:2rem 2.5rem;display:flex;align-items:center;justify-content:space-around;flex-wrap:wrap;gap:1.5rem}
.psb-item{text-align:center;flex:1;min-width:140px}
.psb-num{font-family:var(--font-display);font-size:2rem;font-weight:600;color:var(--rose);line-height:1}
.psb-label{font-size:.75rem;color:var(--muted);margin-top:.4rem}
.psb-div{width:.5px;height:50px;background:var(--border);flex-shrink:0}
.sol-section{background:linear-gradient(180deg,transparent,rgba(45,212,191,.03),transparent);border-top:.5px solid rgba(45,212,191,.12);border-bottom:.5px solid rgba(45,212,191,.12);padding:5rem 0;margin:2rem 0}
.solution-intro{font-size:1.05rem;color:var(--muted2);line-height:1.85;max-width:680px;margin-bottom:3rem}
.sol-flow{display:flex;align-items:stretch;gap:.75rem;flex-wrap:wrap}
.flow-step{flex:1;min-width:220px;background:var(--card);border:.5px solid rgba(45,212,191,.2);border-radius:14px;padding:1.75rem;transition:transform .2s}
.flow-step:hover{transform:translateY(-3px)}
.flow-num{font-family:var(--font-display);font-size:2.5rem;font-weight:600;color:var(--teal);opacity:.35;line-height:1;margin-bottom:.75rem}
.flow-title{font-family:var(--font-display);font-size:1.15rem;font-weight:600;color:#fff;margin-bottom:.6rem}
.flow-desc{font-size:.87rem;color:var(--muted2);line-height:1.75}
.flow-desc em{color:var(--gold2);font-style:italic}
.flow-arrow{font-size:1.5rem;color:var(--teal);opacity:.35;display:flex;align-items:center;flex-shrink:0}
.feat-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1.5rem}
.feat-card{background:var(--card);border:.5px solid var(--border);border-radius:12px;padding:1.75rem;transition:border-color .2s,transform .2s}
.feat-card:hover{border-color:var(--border2);transform:translateY(-3px)}
.feat-ico{font-size:1.75rem;margin-bottom:1rem}
.feat-title{font-family:var(--font-display);font-size:1.2rem;font-weight:600;color:var(--gold2);margin-bottom:.5rem}
.feat-desc{font-size:.88rem;color:var(--muted2);line-height:1.7}
</style>

<div class="sp-hero">
  <div class="hero-eyebrow"><span class="hline"></span> AI-Powered Scholarship Discovery <span class="hline"></span></div>
  <h1 class="sp-h1">Find Your <strong>Scholarship.</strong><span class="line2">Powered by AI, Built for India.</span></h1>
  <p class="hero-desc">Ask in plain language. Get instant, cited answers from 300+ official scholarship documents. Powered by LangChain, Supabase &amp; Groq.</p>
  <div class="hero-actions">
    <a class="btn-gold" href="?page=chat">Ask a Question &#10022;</a>
    <a class="btn-ghost" href="?page=architecture">How It Works</a>
  </div>
  <div class="stats-row">
    <div class="stat-card"><div class="stat-n">&#8377;3000Cr+</div><div class="stat-l">Unclaimed Every Year</div></div>
    <div class="stat-card"><div class="stat-n">307</div><div class="stat-l">Pages Indexed</div></div>
    <div class="stat-card"><div class="stat-n">50+</div><div class="stat-l">Scholarships Covered</div></div>
    <div class="stat-card"><div class="stat-n">Groq</div><div class="stat-l">LLM Backend</div></div>
  </div>
</div>

<div class="section-wrap">
  <span class="sec-eyebrow">The Reality in India</span>
  <div class="sec-title">The <em>Problem</em></div>
  <p class="problem-intro">Every year, thousands of crores in scholarship money goes completely unclaimed. Not because students do not deserve it — but because they simply do not know it exists.</p>
  <div class="problem-grid">
    <div class="problem-card">
      <div class="problem-icon">&#128542;</div>
      <div class="problem-tag">Problem 1</div>
      <div class="problem-title">Information Is Scattered</div>
      <div class="problem-desc">Scholarship details are buried across hundreds of government PDFs, portals, and circulars. A student would need to read 300+ documents just to understand what they qualify for.</div>
    </div>
    <div class="problem-card">
      <div class="problem-icon">&#128336;</div>
      <div class="problem-tag">Problem 2</div>
      <div class="problem-title">Deadlines Are Missed</div>
      <div class="problem-desc">Students miss scholarship deadlines every year — not due to carelessness, but because there is no easy way to find deadlines, eligibility criteria, and required documents all in one place.</div>
    </div>
    <div class="problem-card">
      <div class="problem-icon">&#127760;</div>
      <div class="problem-tag">Problem 3</div>
      <div class="problem-title">Language Barrier</div>
      <div class="problem-desc">Government scholarship documents are written in complex legal language. First-generation students — who need these funds the most — often cannot understand what they are reading, so they give up.</div>
    </div>
    <div class="problem-card">
      <div class="problem-icon">&#128245;</div>
      <div class="problem-tag">Problem 4</div>
      <div class="problem-title">No One to Ask</div>
      <div class="problem-desc">In rural and semi-urban India, students have no mentor to guide them through the scholarship process. They are on their own — and that loneliness costs them thousands of rupees every year.</div>
    </div>
  </div>
  <div class="psb">
    <div class="psb-item"><div class="psb-num">&#8377;3000 Cr+</div><div class="psb-label">Scholarship funds unclaimed annually</div></div>
    <div class="psb-div"></div>
    <div class="psb-item"><div class="psb-num">Millions</div><div class="psb-label">Eligible students who never apply</div></div>
    <div class="psb-div"></div>
    <div class="psb-item"><div class="psb-num">300+</div><div class="psb-label">PDFs a student must read manually</div></div>
  </div>
</div>

<div class="sol-section">
  <div class="section-wrap" style="padding-top:0">
    <span class="sec-eyebrow" style="color:var(--teal)">Enter ScholarPath AI</span>
    <div class="sec-title">The <em>Solution</em></div>
    <p class="solution-intro">We built an AI assistant that has read every single scholarship document — so you do not have to. Ask it anything, in plain language, and get an instant, accurate, cited answer in seconds.</p>
    <div class="sol-flow">
      <div class="flow-step">
        <div class="flow-num">01</div>
        <div class="flow-title">You Ask Naturally</div>
        <div class="flow-desc">Type your question the way you would ask a friend — <em>"I am OBC from Maharashtra, doing engineering. What scholarships can I get?"</em> No forms. No portals. Just ask.</div>
      </div>
      <div class="flow-arrow">&#8594;</div>
      <div class="flow-step">
        <div class="flow-num">02</div>
        <div class="flow-title">AI Searches 307 Pages</div>
        <div class="flow-desc">Our RAG engine instantly searches through 307 pages of official scholarship documents using semantic vector search — finding the most relevant information in milliseconds.</div>
      </div>
      <div class="flow-arrow">&#8594;</div>
      <div class="flow-step">
        <div class="flow-num">03</div>
        <div class="flow-title">You Get a Clear Answer</div>
        <div class="flow-desc">Groq LLM turns the retrieved chunks into a clear, structured answer — with the exact PDF source cited. No guessing. No hallucinations. Just facts.</div>
      </div>
    </div>
    <div style="text-align:center;margin-top:3rem">
      <a class="btn-gold" href="?page=chat">Try It Right Now &#10022;</a>
    </div>
  </div>
</div>

<div class="section-wrap">
  <span class="sec-eyebrow">What Makes It Special</span>
  <div class="sec-title">Built for <em>Real Students</em></div>
  <div class="feat-grid">
    <div class="feat-card"><div class="feat-ico">&#128269;</div><div class="feat-title">Semantic Search</div><div class="feat-desc">Ask naturally. The RAG engine understands meaning, not just keywords.</div></div>
    <div class="feat-card"><div class="feat-ico">&#128196;</div><div class="feat-title">Source Citations</div><div class="feat-desc">Every answer cites the exact PDF it came from. No hallucinations.</div></div>
    <div class="feat-card"><div class="feat-ico">&#9889;</div><div class="feat-title">Semantic Cache</div><div class="feat-desc">Similar questions answered instantly from cache — no repeated LLM calls.</div></div>
    <div class="feat-card"><div class="feat-ico">&#128077;</div><div class="feat-title">Feedback Loop</div><div class="feat-desc">Like an answer and it is stored. The system learns with every interaction.</div></div>
    <div class="feat-card"><div class="feat-ico">&#127470;&#127475;</div><div class="feat-title">India-Focused</div><div class="feat-desc">SC/ST/OBC/EWS, state-wise, income-based — all categories covered.</div></div>
    <div class="feat-card"><div class="feat-ico">&#128483;&#65039;</div><div class="feat-title">Plain Language</div><div class="feat-desc">No jargon. Ask like you would ask a friend. Clear, human answers.</div></div>
  </div>
</div>
""", unsafe_allow_html=True)