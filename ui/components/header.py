import streamlit as st

def show_header():
    st.markdown("""
    <div class="header">
        <h1>Prompt2Anim</h1>
        <p class="subtitle">Turn your ideas into mathematical animations with AI</p>
    </div>
    """, unsafe_allow_html=True)