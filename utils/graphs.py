import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import altair as alt
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

def histogram():
    fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Figure Displayed with fig.show()"
    )
    st.plotly_chart(fig,use_container_width=True)

def scatter(source):
    c=(alt.Chart(source).mark_circle().encode(
    alt.X('sepal_length').scale(zero=False),
    alt.Y('sepal_width').scale(zero=False, padding=0),
    color='species',
    size='petal_width'
    ))
    st.altair_chart(c,use_container_width=True)

def boxPlot():
    df = px.data.tips()
    fig = px.box(df, y="total_bill")
    st.plotly_chart(fig,use_container_width=True)


def pie():
    category = ['Sky', 'Shady side of a pyramid', 'Sunny side of a pyramid']
    color = ["#416D9D", "#674028", "#DEAC58"]
    df = pd.DataFrame({'category': category, 'value': [75, 10, 15]})

    c=(alt.Chart(df).mark_arc(outerRadius=80).encode(
    alt.Theta('value:Q').scale(range=[2.356, 8.639]),
    alt.Color('category:N')
        .title(None)
        .scale(domain=category, range=color)
        .legend(orient='none', legendX=460, legendY=50),
    order='value:Q'
    ).configure_view(
    strokeOpacity=0
    ))
    st.altair_chart(c,use_container_width=True)