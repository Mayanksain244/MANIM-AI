import streamlit as st
from datetime import datetime

def show_footer():
    st.markdown("---")
    st.markdown(f"""
    <div class="footer">
        <div class="footer-content">
            <p>© {datetime.now().year} Prompt2Anim | Created with ❤️ by Your Name</p>
            <div class="social-links">
                <a href="https://github.com/yourusername" target="_blank">GitHub</a>
                <span>•</span>
                <a href="https://linkedin.com/in/yourprofile" target="_blank">LinkedIn</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)