import streamlit as st

from style.style import style
import os
from PIL import Image
import io
import warnings

from utils.graphs import *

warnings.filterwarnings('ignore')

path_file = os.getcwd() + '/images/ikea-logo.png'
logo = Image.open(path_file)


st.set_page_config(
    page_title='Ikea | Dashboard',
    page_icon=logo,
    layout='wide'
)

style()

st.markdown(f'# <img src="https://raw.githubusercontent.com/elghallali/ikea-app-product/master/images/ikea-logo.png" alt="Ikea Logo" width=100/> Ikea Dashboard',unsafe_allow_html=True)

source = px.data.iris()

cols1=st.columns(3)
with cols1[0]:
    histogram()
with cols1[1]:    
    scatter(source)
with cols1[2]:
    histogram()
cols2=st.columns(2)
with cols2[0]:
    boxPlot()
with cols2[1]:
    pie()