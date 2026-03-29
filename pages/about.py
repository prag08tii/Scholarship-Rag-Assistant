import streamlit as st

def render():
    st.markdown("""
<style>
.about-wrap{max-width:820px;margin:0 auto;padding:6rem 2rem;margin-top:68px}
.sec-eyebrow{font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);margin-bottom:1rem;display:block}
.sec-title{font-family:var(--font-display);font-size:clamp(2rem,5vw,3.5rem);font-weight:300;color:#fff;line-height:1.1;margin-bottom:2rem}
.sec-title em{font-style:italic;color:var(--gold2)}
.about-hero{display:flex;gap:2.5rem;align-items:flex-start;margin-bottom:2.5rem;flex-wrap:wrap}
.av{width:90px;height:90px;border-radius:50%;background:var(--goldF);border:.5px solid var(--border2);color:var(--gold2);font-family:var(--font-display);font-size:1.5rem;font-weight:600;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.about-name{font-family:var(--font-display);font-size:2rem;font-weight:600;color:#fff;margin-bottom:.3rem}
.about-role{font-size:.85rem;color:var(--gold);letter-spacing:.08em;text-transform:uppercase;margin-bottom:1rem}
.about-bio{color:var(--muted2);line-height:1.8;font-size:.95rem;margin-bottom:1.25rem}
.pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-bottom:1.5rem}
.pill{font-size:.72rem;padding:.3rem .85rem;border-radius:999px;background:var(--goldF);border:.5px solid var(--border2);color:var(--gold2)}
.social-row{display:flex;gap:.75rem;flex-wrap:wrap}
.social-btn{font-size:.78rem;padding:.5rem 1.25rem;border-radius:6px;background:var(--card2);border:.5px solid var(--border);color:var(--muted2);text-decoration:none;transition:color .2s,border-color .2s}
.social-btn:hover{color:var(--gold2);border-color:var(--gold)}
.mission-box{background:var(--card);border:.5px solid var(--border);border-radius:12px;padding:2rem 2.5rem;margin-top:2.5rem;border-left:2px solid var(--gold)}
.mission-box h3{font-family:var(--font-display);font-size:1.25rem;color:var(--gold2);margin-bottom:1rem}
.mission-box p{color:var(--muted2);line-height:1.9;font-size:.95rem}
</style>

<div class="about-wrap">
  <span class="sec-eyebrow">The Builder</span>
  <div class="sec-title">About <em>Me</em></div>
  <div class="about-hero">
    <div class="av">PG</div>
    <div>
      <div class="about-name">Pragati Gondkar</div>
      <div class="about-role">AI / ML Developer &middot; Nashik, India</div>
      <div class="about-bio">I am a developer passionate about building AI systems that solve real problems in India. ScholarPath AI started as a personal frustration — watching peers miss scholarship deadlines — and became a mission to democratise access to education funding through technology.</div>
      <div class="pills">
        <span class="pill">Python</span>
        <span class="pill">LangChain</span>
        <span class="pill">RAG</span>
        <span class="pill">Supabase</span>
        <span class="pill">Streamlit</span>
        <span class="pill">LLMs</span>
        <span class="pill">pgvector</span>
        <span class="pill">Groq API</span>
      </div>
      <div class="social-row">
        <a class="social-btn" href="#" target="_blank">GitHub</a>
        <a class="social-btn" href="#" target="_blank">LinkedIn</a>
        <a class="social-btn" href="#" target="_blank">Twitter / X</a>
      </div>
    </div>
  </div>
  <div class="mission-box">
    <h3>"Why I built ScholarPath AI"</h3>
    <p>In India, thousands of crores in scholarship money goes unclaimed every year. Students who deserve support do not receive it — not because of lack of merit, but because the information is inaccessible. ScholarPath AI is my attempt to change that: a conversational AI that speaks plain language, cites its sources, learns from feedback, and gets smarter with every interaction.</p>
  </div>
</div>
""", unsafe_allow_html=True)