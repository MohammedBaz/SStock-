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
st.dataframe(df1[X1].corr())


import seaborn as sns
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
colormap = plt.cm.RdBu

plt.title('Single Step AutoCorr', y=1.05, size=16)

mask = np.zeros_like(df1[X1].corr())
mask[np.triu_indices_from(mask)] = True

sns.heatmap(df1[X1].corr(), mask=mask, linewidths=0.1,vmax=1.0, 
            square=True, cmap=colormap, linecolor='white', annot=True)

sns.heatmap(df1[X1].corr(), ax=ax)
st.write(fig)
