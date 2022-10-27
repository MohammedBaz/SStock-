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
sns.lineplot(data=df1, x="date1", y="open")
sns.lineplot(data=df1, x="date1", y="close")
st.pyplot(fig)
