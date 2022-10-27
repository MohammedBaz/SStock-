# Contents of ~/my_app/pages/page_2.py
# the (02) prefix of 02page2.py has been added to ensure the correct sort of pages only 
import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
df = pd.read_csv('out.csv')

option = st.selectbox('Select the Compmay name',df['name'].unique())
df1=df.loc[df['name'] == option]
df1 = df1.rename(columns={'date':'index'}).set_index('index')
chart_data = df1[['open','high','low','close']].copy()
st.area_chart(chart_data)


#chart_data = df1[['open','high','low','close','no_trades ']].copy()

#c = alt.Chart(df1['close'])
#st.altair_chart(c)




