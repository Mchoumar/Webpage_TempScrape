# This is a webpage to present a graph of the acquired data
import streamlit as st
import plotly.express as ex
from data_read import read

# Reads the data
data = read()
temp = [item[1] for item in data]
date = [item[0] for item in data]

# figure setup
figure = ex.line(x=date, y=temp, labels={"x": "Date", "y": "Temperature"})
st.plotly_chart(figure)