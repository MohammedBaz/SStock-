# Contents of ~/my_app/pages/page_2.py
# the (02) prefix of 02page2.py has been added to ensure the correct sort of pages only 
import streamlit as st
import pandas as pd
import numpy as np
df = pd.read_csv('out.csv')
df["date1"] = pd.to_datetime(df["date1"]) 
df =df.sort_values(by='date1')

option = st.selectbox('Select the Compmay name',df['name'].unique())
df1=df.loc[df['name'] == option]

XX=['open','date','high','low','close','volume_traded ',
           'no_trades ','value_traded','dayOfWeek','AMonth','ADay','AYear']

df2=df1.loc[df1['open'].idxmax()];f22 = df2[XX].copy().to_numpy()
df3=df1.loc[df1['close'].idxmax()];f33 = df3[XX].copy().to_numpy()
df4=df1.loc[df1['high'].idxmax()];f44 = df4[XX].copy().to_numpy()
df5=df1.loc[df1['low'].idxmax()];f55 = df5[XX].copy().to_numpy()
df6=df1.loc[df1['open'].idxmin()];f66 = df6[XX].copy().to_numpy()
df7=df1.loc[df1['close'].idxmin()];f77 = df7[XX].copy().to_numpy()
df8=df1.loc[df1['high'].idxmin()];f88 = df8[XX].copy().to_numpy()
df9=df1.loc[df1['low'].idxmin()];f99 = df9[XX].copy().to_numpy()

dataset = pd.DataFrame()
dataset['Title'] = XX
dataset['Opening Price Max'] = f22
dataset['Opening Price Min'] = f66
dataset['Close Price Max'] = f33
dataset['Close Price Min'] = f77
dataset['Highest Price Max'] = f44
dataset['Highest Price Min'] = f88
dataset['Lowest Price Max'] = f55
dataset['Lowest Price Min'] = f99
st.dataframe(dataset)
