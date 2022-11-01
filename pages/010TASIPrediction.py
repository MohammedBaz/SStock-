import numpy as np
import pandas as pd
import streamlit as st
df = pd.read_csv("/content/tasi_d.csv")
df['Date'] =pd.to_datetime(df['Date'])
df=df.sort_values(by=['Date'])
df.set_index('Date',inplace=True, drop=True)
df['Open'] = df['Open'].astype(float)
df['High'] = df['High'].astype(float)
df['Low'] = df['Low'].astype(float)
df['Close'] = df['Close'].astype(float)
df['Volume'] = df['Volume'].astype(float)

def plotCloseVolumeWithButton():
  import plotly.express as px
  from plotly.subplots import make_subplots
  import plotly.graph_objects as go
  fig = make_subplots(rows=2, cols=1, vertical_spacing=0.065, shared_xaxes=True)
  fig.add_trace(
      go.Scatter(name="Close",x=list(df.index), y=list(df.Close)), 1, 1)
  fig.add_trace(
      go.Scatter(name="Volume",x=list(df.index),y=list(df.Volume)), 2, 1);
  fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=[
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ]),
        type="date"),#end xaxis  definition
    
    xaxis2_rangeslider_visible=True,
    xaxis2_type="date"
    );
  st.write(fig)
plotCloseVolumeWithButton
  
