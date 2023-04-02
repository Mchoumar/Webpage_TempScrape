# This is a webpage to present a graph of the acquired data
import streamlit as st
import plotly.express as px
from store import data_read

# Reads the data and filters them
texts = data_read()
date, temp = [], []

# filters the data
for index, text in enumerate(texts):
    if index != 0:
        date.append(text[0])
        temp.append(text[1])

# figure setup
figure = px.line(x=date, y=temp, labels={"x": "Date", "y": "Temperature"})
st.plotly_chart(figure)