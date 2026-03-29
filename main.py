# ============================================================
# main.py  ←  streamlit run main.py
# ============================================================

import streamlit as st

st.set_page_config(
    page_title="ScholarPath AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

from components.navbar import init_theme, inject_theme, render_navbar
from components.footer import render_footer

from pages.home         import render as home_page
from pages.architecture import render as architecture_page
from pages.about        import render as about_page
from pages.ai_chat      import render as chat_page

# 1 — Set default theme
init_theme()

# 2 — Inject CSS colour variables for chosen theme
inject_theme()

# 3 — Current page from URL
current_page = st.query_params.get("page", "home")

# 4 — Navbar (contains the toggle button)
render_navbar(current_page)

# 5 — Page content
PAGE_ROUTER = {
    "home":         home_page,
    "architecture": architecture_page,
    "about":        about_page,
    "chat":         chat_page,
}
PAGE_ROUTER.get(current_page, home_page)()

# 6 — Footer
render_footer()