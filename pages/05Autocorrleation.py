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

X1=['open',	'high',	'low',	'close','volume_traded ','value_traded','no_trades ']
df1[X1].corr()
