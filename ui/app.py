import os
import time
import streamlit as st
from PIL import Image
from pathlib import Path


import sys
import os
# Go 2 levels up to reach the root where main.py exists
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import Prompt2Anim


from ui.components.header import show_header
from ui.components.footer import show_footer

# Set page config
st.set_page_config(
    page_title="Prompt2Anim",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize the animator
@st.cache_resource
def get_animator():
    return Prompt2Anim()

def main():
    # Load assets
    local_css("ui/assets/style.css")
    
    # Show header
    show_header()
    
    # Main content
    st.markdown("""
    <div class="main-container">
        <div class="content-box">
    """, unsafe_allow_html=True)
    
    # Animation prompt input
    with st.form(key='animation_form'):
        prompt = st.text_area(
            "Describe your animation:",
            placeholder="e.g., 'Show a red circle that grows and fades into a blue square'",
            height=150
        )
        
        col1, col2 = st.columns([1, 3])
        with col1:
            quality = st.selectbox(
                "Quality Level",
                ["Low (Fast)", "Medium", "High (Slow)"],
                index=0
            )
        with col2:
            submitted = st.form_submit_button("Generate Animation")
    
    # Animation generation
    if submitted and prompt:
        with st.spinner("Creating your animation..."):
            try:
                animator = get_animator()
                start_time = time.time()
                
                # Generate animation
                video_path = animator.process_prompt(prompt)
                
                # Display results
                st.success(f"Animation generated in {time.time()-start_time:.1f} seconds!")
                
                # Show video
                st.video(video_path)
                
                # Download button
                with open(video_path, "rb") as file:
                    st.download_button(
                        label="Download Animation",
                        data=file,
                        file_name=Path(video_path).name,
                        mime="video/mp4"
                    )
                
            except Exception as e:
                st.error(f"Error generating animation: {str(e)}")
    
    st.markdown("""
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Show footer
    show_footer()

if __name__ == "__main__":
    main()