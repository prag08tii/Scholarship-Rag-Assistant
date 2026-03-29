# ============================================================
# components/navbar.py
# PURPOSE : Fixed gold navbar + single dark/light toggle button
# Used by : main.py
# ============================================================

import streamlit as st


# ── Theme CSS variables ───────────────────────────────────────
THEMES = {
    "dark": """
        --bg0:#060810; --bg1:#0a0d17; --bg2:#0f1422; --bg3:#141929;
        --card:#111623; --card2:#161d30;
        --gold:#c9a84c; --gold2:#e8c97a; --gold3:#f5e0a0;
        --goldF:rgba(201,168,76,0.08); --goldB:rgba(201,168,76,0.18);
        --blue:#4f8ef7; --teal:#2dd4bf; --rose:#f472b6; --green:#34d399;
        --text:#e8eaf0; --muted:#6b7280; --muted2:#9ca3af;
        --border:rgba(201,168,76,0.12); --border2:rgba(201,168,76,0.25);
        --nav-bg:rgba(6,8,16,0.88);
        --font-display:'Cormorant Garamond',Georgia,serif;
        --font-body:'Outfit',sans-serif;
    """,
    "light": """
        --bg0:#f5f3ee; --bg1:#edeae2; --bg2:#e5e0d5; --bg3:#dcd5c7;
        --card:#ffffff; --card2:#f9f6f0;
        --gold:#b5882a; --gold2:#9a6e1a; --gold3:#7a5210;
        --goldF:rgba(181,136,42,0.08); --goldB:rgba(181,136,42,0.18);
        --blue:#2563eb; --teal:#0d9488; --rose:#db2777; --green:#059669;
        --text:#1a1814; --muted:#6b6355; --muted2:#78716c;
        --border:rgba(181,136,42,0.18); --border2:rgba(181,136,42,0.35);
        --nav-bg:rgba(245,243,238,0.92);
        --font-display:'Cormorant Garamond',Georgia,serif;
        --font-body:'Outfit',sans-serif;
    """,
}


def init_theme():
    """Sets dark as default theme on first load. Call once in main.py."""
    if "theme" not in st.session_state:
        st.session_state["theme"] = "dark"


def inject_theme():
    """
    Injects CSS variables for the current theme.
    Call in main.py before render_navbar().
    """
    theme = st.session_state.get("theme", "dark")
    css_vars = THEMES[theme]

    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400&family=Outfit:wght@300;400;500;600&display=swap');
    :root {{ {css_vars} }}

    *, *::before, *::after {{ box-sizing:border-box; margin:0; padding:0; }}
    html, body,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"] {{
      background: var(--bg0) !important;
      color: var(--text) !important;
      font-family: var(--font-body) !important;
      font-weight: 300; overflow-x: hidden;
    }}
    #MainMenu, footer, header         {{ visibility:hidden !important; }}
    .stDeployButton                   {{ display:none !important; }}
    .block-container                  {{ padding:0 !important; max-width:100% !important; }}
    section[data-testid="stSidebar"]  {{ display:none !important; }}
    [data-testid="stAppViewContainer"] > div:first-child {{ padding-top:0 !important; }}
    div[data-testid="stVerticalBlock"] {{ gap:0 !important; }}
    </style>
    """, unsafe_allow_html=True)


def render_navbar(current_page: str):
    """
    Draws the navbar.
    The 🌙/☀️ toggle is a single Streamlit button injected
    into the navbar via CSS fixed positioning.
    """

    current_theme = st.session_state.get("theme", "dark")
    # Moon when dark (click → go light), Sun when light (click → go dark)
    toggle_icon = "🌙" if current_theme == "dark" else "☀️"

    nav_items = [
        ("Home",         "home"),
        ("Architecture", "architecture"),
        ("About",        "about"),
        ("Ask AI ✦",     "chat"),
    ]

    links_html = ""
    for label, key in nav_items:
        active = "active"  if key == current_page else ""
        cta    = "nav-cta" if key == "chat"        else ""
        links_html += f'<a class="{active} {cta}" href="?page={key}">{label}</a>'

    # ── Navbar HTML (visual shell) ────────────────────────────
    st.markdown(f"""
    <style>
    .sp-nav {{
      position:fixed; top:0; left:0; right:0; z-index:9999;
      height:68px;
      display:flex; align-items:center; justify-content:space-between;
      padding:0 2.5rem;
      background:var(--nav-bg);
      backdrop-filter:blur(24px) saturate(180%);
      border-bottom:0.5px solid var(--border);
    }}
    .sp-brand {{
      font-family:var(--font-display); font-size:1.45rem;
      font-weight:600; letter-spacing:0.02em;
      color:var(--text); text-decoration:none;
      display:flex; align-items:center; gap:0.6rem;
    }}
    .sp-brand em {{ font-style:italic; color:var(--gold2); }}
    .brand-dot {{
      width:7px; height:7px; border-radius:50%;
      background:var(--gold); box-shadow:0 0 10px var(--gold);
      animation:pulse 2s ease-in-out infinite;
    }}
    @keyframes pulse {{ 0%,100%{{opacity:1;transform:scale(1)}} 50%{{opacity:0.5;transform:scale(0.85)}} }}

    .nav-links {{ display:flex; align-items:center; gap:0.1rem; }}
    .nav-links a {{
      font-size:0.78rem; font-weight:400;
      letter-spacing:0.1em; text-transform:uppercase;
      color:var(--muted); text-decoration:none;
      padding:0.45rem 0.9rem; border-radius:6px;
      transition:color 0.2s; position:relative;
    }}
    .nav-links a::after {{
      content:''; position:absolute; bottom:4px; left:50%; right:50%;
      height:1px; background:var(--gold);
      transition:left 0.25s, right 0.25s;
    }}
    .nav-links a:hover, .nav-links a.active {{ color:var(--gold2); }}
    .nav-links a:hover::after, .nav-links a.active::after {{ left:0.9rem; right:0.9rem; }}
    .nav-cta {{
      font-weight:500 !important; color:var(--bg0) !important;
      background:var(--gold) !important; border-radius:6px !important;
      padding:0.5rem 1.2rem !important;
    }}
    .nav-cta::after {{ display:none !important; }}
    .nav-cta:hover {{ background:var(--gold2) !important; color:#000 !important; }}

    /* ── The toggle button injected into navbar ── */
    .theme-toggle-wrap {{
      position:fixed; top:14px; right:2.5rem; z-index:10001;
    }}
    .theme-toggle-wrap div.stButton > button {{
      width:40px !important; height:40px !important;
      border-radius:50% !important;
      background:var(--card) !important;
      border:0.5px solid var(--border2) !important;
      color:var(--text) !important;
      font-size:1.1rem !important;
      padding:0 !important;
      display:flex !important; align-items:center !important; justify-content:center !important;
      cursor:pointer !important;
      transition:background 0.2s, transform 0.15s, border-color 0.2s !important;
      box-shadow:0 2px 12px rgba(0,0,0,0.18) !important;
    }}
    .theme-toggle-wrap div.stButton > button:hover {{
      background:var(--goldF) !important;
      border-color:var(--gold) !important;
      transform:scale(1.08) !important;
    }}
    </style>

    <nav class="sp-nav">
      <a class="sp-brand" href="?page=home">
        <div class="brand-dot"></div>
        Scholar<em>Path</em> AI
      </a>
      <div class="nav-links">{links_html}</div>
    </nav>

    <!-- spacer so page content doesn't hide under fixed navbar -->
    <div style="height:68px"></div>
    """, unsafe_allow_html=True)

    # ── Single toggle button — positioned into navbar via CSS ─
    st.markdown('<div class="theme-toggle-wrap">', unsafe_allow_html=True)
    if st.button(toggle_icon, key="theme_toggle"):
        # Flip between dark and light
        st.session_state["theme"] = "light" if current_theme == "dark" else "dark"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)