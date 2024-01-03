import streamlit as st
import pandas as pd
import os

from style.style import style
from PIL import Image
import io
import warnings

warnings.filterwarnings('ignore')

path_file = os.getcwd() + '/images/ikea-logo.png'
logo = Image.open(path_file)


st.set_page_config(
    page_title='Ikea | Home',
    page_icon=logo,
    layout='wide'
)

style()

st.markdown(f'# <img src="" alt="Ikea Logo" width=100/> Ikea App Home',unsafe_allow_html=True)

