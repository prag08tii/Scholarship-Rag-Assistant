# ============================================================
# components/theme.py
# PURPOSE : All CSS for the luxury dark-gold theme
# Used by : main.py  (injected once, applies to every page)
# ============================================================

def load_theme() -> str:
    """Returns the complete <style> block as a string."""
    return """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400&family=Outfit:wght@300;400;500;600&display=swap');

/* ══════════════════════════════════════════
   DESIGN SYSTEM — LUXURY DARK GOLD
   Aesthetic: Editorial · Refined · Cinematic
══════════════════════════════════════════ */
:root {
  --bg0: #060810; --bg1: #0a0d17; --bg2: #0f1422; --bg3: #141929;
  --card: #111623; --card2: #161d30;
  --gold: #c9a84c; --gold2: #e8c97a; --gold3: #f5e0a0;
  --goldF: rgba(201,168,76,0.08); --goldB: rgba(201,168,76,0.18);
  --blue: #4f8ef7; --teal: #2dd4bf; --rose: #f472b6; --green: #34d399;
  --text: #e8eaf0; --muted: #6b7280; --muted2: #9ca3af;
  --border: rgba(201,168,76,0.12); --border2: rgba(201,168,76,0.25);
  --font-display: 'Cormorant Garamond', Georgia, serif;
  --font-body: 'Outfit', sans-serif;
}

/* ── Hide ALL Streamlit default chrome ── */
#MainMenu, footer, header            { visibility: hidden !important; }
.stDeployButton                      { display: none !important; }
.block-container                     { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"]     { display: none !important; }
[data-testid="stAppViewContainer"] > div:first-child { padding-top: 0 !important; }
div[data-testid="stVerticalBlock"]   { gap: 0 !important; }

/* ── Global base ── */
html, body,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
  background: var(--bg0) !important;
  color: var(--text) !important;
  font-family: var(--font-body) !important;
  font-weight: 300;
  overflow-x: hidden;
}

/* Grain overlay — the subtle film texture */
body::before {
  content: '';
  position: fixed; inset: 0; z-index: 0; pointer-events: none;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
  opacity: 0.35;
}

/* ══════════════════ NAVBAR ══════════════════ */
.sp-nav {
  position: fixed; top: 0; left: 0; right: 0; z-index: 9999;
  height: 68px;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 3rem;
  background: rgba(6,8,16,0.88);
  backdrop-filter: blur(24px) saturate(180%);
  border-bottom: 0.5px solid var(--border);
}
.sp-brand {
  font-family: var(--font-display); font-size: 1.45rem;
  font-weight: 600; letter-spacing: 0.02em;
  color: #fff; text-decoration: none;
  display: flex; align-items: center; gap: 0.6rem;
}
.sp-brand em { font-style: italic; color: var(--gold2); }
.brand-dot {
  width: 7px; height: 7px; border-radius: 50%;
  background: var(--gold); box-shadow: 0 0 10px var(--gold);
  animation: pulse 2s ease-in-out infinite;
}
@keyframes pulse { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:0.5;transform:scale(0.85)} }

.nav-links { display: flex; align-items: center; gap: 0.15rem; }
.nav-links a {
  font-size: 0.78rem; font-weight: 400;
  letter-spacing: 0.1em; text-transform: uppercase;
  color: var(--muted); text-decoration: none;
  padding: 0.45rem 1rem; border-radius: 6px;
  transition: color 0.2s;
  position: relative;
}
.nav-links a::after {
  content: ''; position: absolute; bottom: 4px; left: 50%; right: 50%;
  height: 1px; background: var(--gold);
  transition: left 0.25s, right 0.25s;
}
.nav-links a:hover, .nav-links a.active { color: var(--gold2); }
.nav-links a:hover::after, .nav-links a.active::after { left: 1rem; right: 1rem; }
.nav-cta {
  font-weight: 500 !important; color: var(--bg0) !important;
  background: var(--gold) !important; border-radius: 6px !important;
  padding: 0.5rem 1.35rem !important; letter-spacing: 0.08em !important;
}
.nav-cta::after { display: none !important; }
.nav-cta:hover { background: var(--gold2) !important; color: #000 !important; }

/* ══════════════════ HERO ══════════════════ */
.sp-hero {
  min-height: calc(100vh - 68px);
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  text-align: center; padding: 5rem 1.5rem 4rem;
  margin-top: 68px; position: relative; overflow: hidden;
}
.sp-hero::before {
  content: '';
  position: absolute; top: 50%; left: 50%;
  transform: translate(-50%, -60%);
  width: 900px; height: 600px;
  background: radial-gradient(ellipse, rgba(201,168,76,0.07) 0%, transparent 65%);
  pointer-events: none;
}
.hero-eyebrow {
  display: inline-flex; align-items: center; gap: 0.75rem;
  font-size: 0.72rem; letter-spacing: 0.2em; text-transform: uppercase;
  color: var(--gold); border: 0.5px solid var(--border2);
  border-radius: 999px; padding: 0.4rem 1.25rem; margin-bottom: 2.25rem;
  animation: fadeUp 0.6s ease both;
}
.hero-eyebrow .hline { width: 20px; height: 0.5px; background: var(--gold); opacity: 0.5; display: inline-block; }
.sp-h1 {
  font-family: var(--font-display);
  font-size: clamp(3.2rem, 7vw, 6.5rem);
  font-weight: 300; line-height: 1.05; color: #fff;
  animation: fadeUp 0.6s 0.1s ease both;
}
.sp-h1 strong {
  font-weight: 600; font-style: italic;
  background: linear-gradient(135deg, var(--gold2), var(--gold3));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.sp-h1 .line2 { color: rgba(255,255,255,0.45); font-weight: 300; display: block; }
.hero-desc {
  max-width: 520px; margin: 2rem auto 3rem;
  font-size: 1rem; font-weight: 300; color: var(--muted2); line-height: 1.8;
  animation: fadeUp 0.6s 0.2s ease both;
}
.hero-actions {
  display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;
  animation: fadeUp 0.6s 0.3s ease both;
}
.btn-gold {
  background: var(--gold); color: #060810;
  border: none; padding: 0.85rem 2.25rem; border-radius: 8px;
  font-family: var(--font-body); font-size: 0.88rem;
  font-weight: 600; letter-spacing: 0.04em; cursor: pointer;
  text-transform: uppercase; text-decoration: none;
  transition: background 0.2s, transform 0.15s; display: inline-block;
}
.btn-gold:hover { background: var(--gold2); transform: translateY(-2px); color: #000; }
.btn-ghost {
  background: transparent; color: var(--gold);
  border: 0.5px solid var(--border2); padding: 0.85rem 2.25rem;
  border-radius: 8px; font-family: var(--font-body);
  font-size: 0.88rem; letter-spacing: 0.04em; cursor: pointer;
  text-transform: uppercase; text-decoration: none;
  transition: border-color 0.2s, color 0.2s; display: inline-block;
}
.btn-ghost:hover { border-color: var(--gold2); color: var(--gold2); }

/* Stats row */
.stats-row {
  display: flex; gap: 2px; justify-content: center;
  margin-top: 5rem; flex-wrap: wrap;
}
.stat-card {
  background: var(--card); border: 0.5px solid var(--border);
  padding: 1.75rem 2.5rem; text-align: center; flex: 1; min-width: 150px;
}
.stat-card:first-child { border-radius: 12px 0 0 12px; }
.stat-card:last-child  { border-radius: 0 12px 12px 0; }
.stat-n {
  font-family: var(--font-display); font-size: 2.4rem;
  font-weight: 600; color: var(--gold2); line-height: 1;
}
.stat-l { font-size: 0.72rem; letter-spacing: 0.12em; text-transform: uppercase; color: var(--muted); margin-top: 0.5rem; }

/* ══════════════════ SHARED SECTION ══════════════════ */
.section-wrap { max-width: 900px; margin: 0 auto; padding: 6rem 2rem; margin-top: 68px; }
.sec-eyebrow {
  font-size: 0.72rem; letter-spacing: 0.2em; text-transform: uppercase;
  color: var(--gold); margin-bottom: 1rem; display: block;
}
.sec-title {
  font-family: var(--font-display); font-size: clamp(2rem, 5vw, 3.5rem);
  font-weight: 300; color: #fff; line-height: 1.1; margin-bottom: 3rem;
}
.sec-title em { font-style: italic; color: var(--gold2); }

/* Feature cards */
.feat-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.5rem; }
.feat-card {
  background: var(--card); border: 0.5px solid var(--border);
  border-radius: 12px; padding: 1.75rem;
  transition: border-color 0.2s, transform 0.2s;
}
.feat-card:hover { border-color: var(--border2); transform: translateY(-3px); }
.feat-ico { font-size: 1.75rem; margin-bottom: 1rem; }
.feat-title { font-family: var(--font-display); font-size: 1.2rem; font-weight: 600; color: var(--gold2); margin-bottom: 0.5rem; }
.feat-desc { font-size: 0.88rem; color: var(--muted2); line-height: 1.7; }

/* ══════════════════ PIPELINE ══════════════════ */
.pipeline-stage {
  background: var(--card); border: 0.5px solid var(--border);
  border-radius: 12px; padding: 1.5rem 2rem;
}
.stage-label {
  font-size: 0.72rem; letter-spacing: 0.15em; text-transform: uppercase;
  color: var(--gold); margin-bottom: 1rem;
  display: flex; align-items: center; gap: 0.75rem;
}
.stage-label::before {
  content: attr(data-n);
  width: 24px; height: 24px; border-radius: 50%;
  background: var(--goldF); border: 0.5px solid var(--border2);
  color: var(--gold2); font-size: 0.78rem;
  display: flex; align-items: center; justify-content: center; flex-shrink: 0;
}
.stage-nodes { display: flex; gap: 1rem; flex-wrap: wrap; }
.node { flex: 1; min-width: 140px; padding: 1rem; border-radius: 8px; border: 0.5px solid transparent; }
.node.blue  { background: rgba(79,142,247,0.07);  border-color: rgba(79,142,247,0.2);  }
.node.green { background: rgba(52,211,153,0.07);  border-color: rgba(52,211,153,0.2);  }
.node.teal  { background: rgba(45,212,191,0.07);  border-color: rgba(45,212,191,0.2);  }
.node.rose  { background: rgba(244,114,182,0.07); border-color: rgba(244,114,182,0.2); }
.node-ico   { font-size: 1.3rem; margin-bottom: 0.4rem; }
.node-name  { font-size: 0.85rem; font-weight: 500; color: var(--text); }
.node-desc  { font-size: 0.75rem; color: var(--muted); margin-top: 0.25rem; }
.stage-arrow { text-align: center; color: var(--border2); font-size: 1.5rem; padding: 0.5rem; }

/* Tech row */
.tech-row { display: flex; flex-wrap: wrap; gap: 1rem; margin-top: 1.5rem; }
.tech-item {
  display: flex; align-items: center; gap: 0.75rem;
  background: var(--card); border: 0.5px solid var(--border);
  border-radius: 8px; padding: 0.85rem 1.25rem; flex: 1; min-width: 160px;
}
.tech-ico  { font-size: 1.5rem; }
.tech-name { font-size: 0.88rem; font-weight: 500; color: var(--text); }
.tech-role { font-size: 0.75rem; color: var(--muted); }

/* ══════════════════ ABOUT ══════════════════ */
.about-wrap { max-width: 820px; margin: 0 auto; padding: 6rem 2rem; margin-top: 68px; }
.about-hero { display: flex; gap: 2.5rem; align-items: flex-start; margin-bottom: 2.5rem; flex-wrap: wrap; }
.av {
  width: 90px; height: 90px; border-radius: 50%;
  background: var(--goldF); border: 0.5px solid var(--border2);
  color: var(--gold2); font-family: var(--font-display);
  font-size: 1.5rem; font-weight: 600;
  display: flex; align-items: center; justify-content: center; flex-shrink: 0;
}
.about-info h2 { font-family: var(--font-display); font-size: 2rem; font-weight: 600; color: #fff; }
.about-role { font-size: 0.85rem; color: var(--gold); letter-spacing: 0.08em; text-transform: uppercase; margin: 0.5rem 0 1rem; }
.about-info p { color: var(--muted2); line-height: 1.8; font-size: 0.95rem; }
.pills { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1.25rem; }
.pill {
  font-size: 0.72rem; padding: 0.3rem 0.85rem; border-radius: 999px;
  background: var(--goldF); border: 0.5px solid var(--border2); color: var(--gold2);
}
.social-row { display: flex; gap: 0.75rem; margin-top: 1.5rem; flex-wrap: wrap; }
.social-btn {
  font-size: 0.78rem; padding: 0.5rem 1.25rem; border-radius: 6px;
  background: var(--card2); border: 0.5px solid var(--border);
  color: var(--muted2); text-decoration: none;
  transition: color 0.2s, border-color 0.2s;
}
.social-btn:hover { color: var(--gold2); border-color: var(--gold); }
.mission-box {
  background: var(--card); border: 0.5px solid var(--border);
  border-radius: 12px; padding: 2rem 2.5rem; margin-top: 2.5rem;
  border-left: 2px solid var(--gold);
}
.mission-box h3 { font-family: var(--font-display); font-size: 1.25rem; color: var(--gold2); margin-bottom: 1rem; }
.mission-box p { color: var(--muted2); line-height: 1.9; font-size: 0.95rem; }

/* ══════════════════ CHAT PAGE ══════════════════ */
.chat-wrap {
  max-width: 820px; margin: 0 auto;
  padding: 2rem 1.5rem 5rem; margin-top: 68px;
}
.chat-top { text-align: center; margin-bottom: 2rem; }
.chat-top h2 { font-family: var(--font-display); font-size: 2.4rem; font-weight: 300; color: #fff; }
.chat-top p  { color: var(--muted2); font-size: 0.95rem; margin-top: 0.5rem; }

/* Chat bubbles rendered by our custom HTML */
.sp-chat-box { display: flex; flex-direction: column; gap: 1.25rem; padding-bottom: 1rem; }
.sp-msg { display: flex; gap: 0.75rem; align-items: flex-start; }
.sp-msg.user { flex-direction: row-reverse; }
.sp-av {
  width: 34px; height: 34px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 0.72rem; font-weight: 600; flex-shrink: 0;
}
.sp-av.bot { background: var(--goldF); border: 0.5px solid var(--border2); color: var(--gold2); }
.sp-av.usr { background: rgba(79,142,247,0.15); border: 0.5px solid rgba(79,142,247,0.3); color: var(--blue); }
.sp-bubble {
  background: var(--card2); border: 0.5px solid var(--border);
  border-radius: 12px; padding: 0.9rem 1.1rem;
  font-size: 0.92rem; line-height: 1.7; color: var(--text); max-width: 85%;
}
.sp-msg.user .sp-bubble { background: var(--goldF); border-color: var(--border2); }
.sp-src-pill {
  display: inline-block; margin-top: 0.5rem;
  font-size: 0.72rem; color: var(--teal);
  border: 0.5px solid rgba(45,212,191,0.25);
  border-radius: 999px; padding: 0.2rem 0.75rem;
}
.sp-cache-pill {
  display: inline-block; margin-top: 0.5rem;
  font-size: 0.72rem; color: var(--gold2);
  border: 0.5px solid var(--border2);
  border-radius: 999px; padding: 0.2rem 0.75rem;
}

/* Quick-chip suggestion buttons */
div.stButton > button {
  background: var(--card2) !important;
  border: 0.5px solid var(--border) !important;
  color: var(--muted2) !important;
  border-radius: 999px !important;
  font-family: var(--font-body) !important;
  font-size: 0.78rem !important;
  padding: 0.4rem 0.9rem !important;
  transition: color 0.2s, border-color 0.2s !important;
  white-space: nowrap !important;
}
div.stButton > button:hover {
  color: var(--gold2) !important;
  border-color: var(--gold) !important;
  background: var(--goldF) !important;
}

/* Action buttons row (like/dislike/copy/regen) */
.action-row { display: flex; gap: 0.4rem; margin-top: 0.5rem; }
.act-btn {
  font-size: 0.8rem; padding: 0.28rem 0.6rem;
  border-radius: 6px; background: var(--card2);
  border: 0.5px solid var(--border); cursor: pointer;
  color: var(--muted); transition: color 0.2s, border-color 0.2s;
}
.act-btn:hover { color: var(--gold2); border-color: var(--gold); }

/* Streamlit chat input — style the native widget */
[data-testid="stChatInput"] {
  background: var(--card) !important;
  border: 0.5px solid var(--border) !important;
  border-radius: 12px !important;
}
[data-testid="stChatInput"] textarea {
  background: transparent !important; color: var(--text) !important;
  font-family: var(--font-body) !important;
}
[data-testid="stChatInput"] button { background: var(--gold) !important; border-radius: 8px !important; }

/* Streamlit spinner */
[data-testid="stSpinner"] p { color: var(--muted2) !important; font-size: 0.85rem !important; }

/* Streamlit toast */
[data-testid="stToast"] {
  background: var(--card2) !important; border: 0.5px solid var(--border2) !important;
  color: var(--text) !important;
}

/* Streamlit expander (Sources) */
[data-testid="stExpander"] {
  background: var(--card) !important; border: 0.5px solid var(--border) !important;
  border-radius: 8px !important;
}
[data-testid="stExpander"] summary { color: var(--teal) !important; font-size: 0.82rem !important; }

/* ══════════════════ FOOTER ══════════════════ */
.sp-footer {
  border-top: 0.5px solid var(--border); background: var(--bg0);
  padding: 2.5rem 3rem;
  display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem;
}
.footer-brand { font-family: var(--font-display); font-size: 1.1rem; color: var(--gold2); }
.footer-copy  { font-size: 0.75rem; color: var(--muted); }
.footer-links { display: flex; gap: 1.5rem; }
.footer-links a { font-size: 0.78rem; color: var(--muted); text-decoration: none; transition: color 0.2s; }
.footer-links a:hover { color: var(--gold2); }

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(18px); }
  to   { opacity: 1; transform: translateY(0); }
}
</style>
"""