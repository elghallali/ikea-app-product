import streamlit as st

def style():
    st.markdown("""

<style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}  

        div.block-container {padding-top: 0.1rem;} 
</style>


""",unsafe_allow_html=True)