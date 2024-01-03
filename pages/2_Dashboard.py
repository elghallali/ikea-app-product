import streamlit as st

from style.style import style
import os
from PIL import Image
import io
import warnings

warnings.filterwarnings('ignore')

path_file = os.getcwd() + '/images/ikea-logo.png'
logo = Image.open(path_file)


st.set_page_config(
    page_title='Ikea | Dashboard',
    page_icon=logo,
    layout='wide'
)

style()

st.markdown(f'# <img src="" alt="Ikea Logo" width=100/> Ikea Dashboard',unsafe_allow_html=True)
