import streamlit as st
import duckdb
from etl.data import factTable,ikea
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

data=factTable(ikea)
duckdb_connection = duckdb.connect()
cols1=st.columns(3)
with cols1[0]:
    price=f'''
SELECT name AS Produits,price AS Price FROM data 
GROUP BY name , price
'''
    price_for_products=duckdb_connection.execute(price).df()
    histogram(x=price_for_products['Produits'],y=price_for_products['Price'],title='prix par produit')

    
#with cols1[1]:    
    #scatter()
with cols1[2]:
    price=f'''
SELECT name AS Produits, category AS Category FROM data 
GROUP BY name , category
'''
    name_category=duckdb_connection.execute(price).df()
    histogram(x=name_category['Category'],y=name_category['Produits'],title='Categorie des produits')

cols2=st.columns(2)
with cols2[0]:
    box=f'''
SELECT price AS prix, category AS Category FROM data 
GROUP BY price , category
'''
    price_for_category=duckdb_connection.execute(box).df()
    boxPlot(x=price_for_category['prix'],y=price_for_category['Category'],df=price_for_category)
    
with cols2[1]:
    category = ['Sky', 'Shady side of a pyramid', 'Sunny side of a pyramid']
    df = pd.DataFrame({'category': category, 'value': [75, 10, 15]})
    pie(df,'category','value')