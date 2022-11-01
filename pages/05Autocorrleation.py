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
lag = st.slider('Select number of lags', 1, len(df1)-1, 1)

         
         
X1=['open',	'high',	'low',	'close','volume_traded ','value_traded','no_trades ']
st.dataframe(df1[X1].corr())


import seaborn as sns
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
colormap = plt.cm.RdBu

plt.title('Single Step AutoCorr', y=1.05, size=16)

mask = np.zeros_like(df1[X1].corr(lag))
mask[np.triu_indices_from(mask)] = True

sns.heatmap(df1[X1].corr(), mask=mask, linewidths=0.1,vmax=1.0, 
            square=True, cmap=colormap, linecolor='white', annot=True,ax=ax)

#sns.heatmap(df1[X1].corr(), ax=ax)
st.write(fig)

st.write('Open price One day Autocorrelation',df1['open'].autocorr(lag=1))
st.write('Open price One week Autocorrelation',df1['open'].autocorr(lag=7))
st.write('Open price One month Autocorrelation',df1['open'].autocorr(lag=30))
st.write('Open price One year Autocorrelation',df1['open'].autocorr(lag=365))

st.write('Close price One day Autocorrelation',df1['close'].autocorr(lag=1))
st.write('Close price One week Autocorrelation',df1['close'].autocorr(lag=7))
st.write('Close price One month Autocorrelation',df1['close'].autocorr(lag=30))
st.write('Close price One year Autocorrelation',df1['close'].autocorr(lag=365))

st.write('highest price One day Autocorrelation',df1['high'].autocorr(lag=1))
st.write('highest price One week Autocorrelation',df1['high'].autocorr(lag=7))
st.write('highest price One month Autocorrelation',df1['high'].autocorr(lag=30))
st.write('Open price One year Autocorrelation',df1['high'].autocorr(lag=365))

st.write('Lowest price One day Autocorrelation',df1['low'].autocorr(lag=1))
st.write('Lowest price One week Autocorrelation',df1['low'].autocorr(lag=7))
st.write('Lowest price One month Autocorrelation',df1['low'].autocorr(lag=30))
st.write('Lowest price One year Autocorrelation',df1['low'].autocorr(lag=365))
