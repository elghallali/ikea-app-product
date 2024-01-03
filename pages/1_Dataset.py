import streamlit as st
import pandas as pd
import os
import io
from etl.data import factTable, ikea
from style.style import style
from PIL import Image
import io
import warnings

warnings.filterwarnings('ignore')

path_file = os.getcwd() + '/images/ikea-logo.png'
logo = Image.open(path_file)

st.set_page_config(
    page_title='Ikea | Dataset',
    page_icon=logo,
    layout='wide'
)

style()
data = ikea


st.markdown(f'# <img src="" alt="Ikea Logo" width=100/> Ikea EDA',unsafe_allow_html=True)



st.header('Dataset')

def visualDataFrame(df):
    options = st.multiselect(
        '',
        list(df.columns),list(df.columns))
    tab1, tab2, tab3, tab4 = st.tabs([":card_file_box: Data", "Types", 'NAN', 'Info'])
    with tab1:
        st.subheader("A tab with a data")
        st.dataframe(df[options])
    with tab2:
        st.subheader("Column type :")
        st.text(df[options].dtypes)
    with tab3:
        st.subheader("Null values :")
        st.text(df[options].isna().sum())
    with tab4:
        st.subheader('DataFrame Info')
        buffer = io.StringIO()
        df[options].info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)
    
visualDataFrame(ikea)

st.header('Dataset après ETL Process')
visualDataFrame(factTable(ikea))