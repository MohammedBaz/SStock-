# Contents of ~/my_app/pages/page_2.py
# the (02) prefix of 02page2.py has been added to ensure the correct sort of pages only 
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

fig, ax = plt.subplots()
ax= sns.lineplot(data=df1, x="date1", y="open")
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
ax.set_xlabel('Date')  
ax.yaxis.set_label_text('Opening price')
st.pyplot(plt)

fig, ax = plt.subplots()
ax1= sns.lineplot(data=df1, x="date1", y="close")
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
ax.set_xlabel('Date')  
ax.yaxis.set_label_text('Closing price')
st.pyplot(plt)

fig, ax = plt.subplots()
ax2= sns.lineplot(data=df1, x="date1", y="high")
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
ax.set_xlabel('Date')  
ax.yaxis.set_label_text('Highest price')
st.pyplot(plt)

fig, ax = plt.subplots()
ax3= sns.lineplot(data=df1, x="date1", y="low")
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
ax.set_xlabel('Date')    
ax.yaxis.set_label_text('Lowest price')
st.pyplot(plt)

fig, ax = plt.subplots()
ax1= sns.lineplot(data=df1, x="date1", y="volume_traded ")
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
ax.set_xlabel('Date')   
ax.yaxis.set_label_text('Traded Volume')
st.pyplot(plt)

fig, ax = plt.subplots()
ax2= sns.lineplot(data=df1, x="date1", y="no_trades ")
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
ax.set_xlabel('Date')   
ax.yaxis.set_label_text('Number of Trades')
st.pyplot(plt)

fig, ax = plt.subplots()
ax3= sns.lineplot(data=df1, x="date1", y="value_traded")
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
ax.set_xlabel('Date')    
ax.yaxis.set_label_text('Trading price')
st.pyplot(plt)

