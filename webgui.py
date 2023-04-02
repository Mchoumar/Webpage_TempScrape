# This is a webpage to present a graph of the acquired data
import streamlit as st
import plotly.express as ex
import pandas as px

# Reads the data
data = px.read_csv("data.txt")

# figure setup
figure = ex.line(x=data['date'], y=data['temperature'], labels={"x": "Date", "y": "Temperature"})
st.plotly_chart(figure)