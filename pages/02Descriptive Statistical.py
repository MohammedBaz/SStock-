# Contents of ~/my_app/pages/page_2.py
# the (02) prefix of 02page2.py has been added to ensure the correct sort of pages only 
import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('out.csv')

option = st.selectbox('Select the Compmay name',df['name'].unique())
df1=df.loc[df['name'] == option]
df1 = df1.rename(columns={'date':'index'}).set_index('index')
values = st.slider('Select a range of dates', int(df1.index[0]['date']), int(df1.index[0]['date']), (25.0, 75.0))

st.write('Values:', values)


chart_data = df1[['open','high','low','close','volume_traded ','no_trades ']].copy()
plt.figure()
chart_data.plot(subplots=True, figsize=(6, 6))
plt.legend(loc='best');plt.xticks(rotation=90) # for more plot option see https://pandas.pydata.org/pandas-docs/version/0.13/visualization.html
st.pyplot(plt)


