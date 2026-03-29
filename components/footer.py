# ============================================================
# components/footer.py
# PURPOSE : Footer — shown on EVERY page
# Used by : main.py
# ============================================================

import streamlit as st

def render_footer():
    """Draws the slim dark-gold footer."""
    st.markdown("""
    <footer class="sp-footer">
      <div class="footer-brand">Scholar<em style="font-style:italic;">Path</em> AI</div>
      <div class="footer-copy">© 2025 · Built with LangChain, Supabase &amp; Groq · Nashik, India</div>
      <div class="footer-links">
        <a href="?page=home">Home</a>
        <a href="?page=architecture">Architecture</a>
        <a href="?page=about">About</a>
        <a href="?page=chat">Try AI</a>
      </div>
    </footer>
    """, unsafe_allow_html=True)