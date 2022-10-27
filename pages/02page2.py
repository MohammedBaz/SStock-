# Contents of ~/my_app/pages/page_2.py
# the (02) prefix of 02page2.py has been added to ensure the correct sort of pages only 
import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
df = pd.read_csv('out.csv')

option = st.selectbox('Select the Compmay name',df['name'].unique())
df1=df.loc[df['name'] == option]
#df1 = df1.rename(columns={'date':'index'}).set_index('index')
chart1 = alt.Chart(df1).mark_line().encode(
    x=alt.X('date',axis=alt.Axis(format='%Y-%m',labelAngle=-20)),
    y=alt.Y('close',scale=alt.Scale(domain=[np.min(df1.colname1), np.max(df1.colname1)])), 
).properties(width=500, height=300)
chart2 = alt.Chart(df1).mark_line().encode(
    x=alt.X('date',axis=alt.Axis(format='%Y-%m',labelAngle=-20)),
    y=alt.Y('open',scale=alt.Scale(domain=[np.min(df1.colname2), np.max(df1.colname2)])), 
).properties(width=500, height=300)
st.altair_chart(chart1 | chart2)

#chart_data = df1[['open','high','low','close','no_trades ']].copy()

#c = alt.Chart(df1['close'])
#st.altair_chart(c)




