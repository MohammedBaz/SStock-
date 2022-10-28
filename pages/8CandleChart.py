import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
import seaborn as sns

df = pd.read_csv('out.csv')
df["date1"] = pd.to_datetime(df["date1"]) 
df =df.sort_values(by='date1')

option = st.selectbox('Select the Compmay name',df['name'].unique())
df1=df.loc[df['name'] == option]

fig = go.Figure(data=[go.Candlestick(x=df1['date1'],
                open=df1['open'],
                high=df1['high'],
                low=df1['low'],
                close=df1['close'])])

st.write(fig)
