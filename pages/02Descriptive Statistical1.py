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
chart_data = df1[['open','high','low','close','volume_traded ','no_trades ']].copy()
plt.figure()
chart_data.plot(subplots=True, figsize=(6, 6))
plt.legend(loc='best');plt.xticks(rotation=90) # for more plot option see https://pandas.pydata.org/pandas-docs/version/0.13/visualization.html
st.pyplot(plt)

dchart_data = pd.DataFrame(chart_data.describe(include='all'))
st.dataframe(dchart_data)  # Same as st.write(df)
st.write('One day Autocorrelation',chart_data['open'].autocorr(lag=1))
st.write('One week Autocorrelation',chart_data['open'].autocorr(lag=7))
st.write('One month Autocorrelation',chart_data['open'].autocorr(lag=30))
st.write('One year Autocorrelation',chart_data['open'].autocorr(lag=365))

from statsmodels.tsa.stattools import adfuller
adft = adfuller(df1['open'],autolag="AIC")
output_df = pd.DataFrame({"Values":[adft[0],adft[1],adft[2],adft[3], adft[4]['1%'], adft[4]['5%'], adft[4]['10%']]  , "Metric":["Test Statistics","p-value","No. of lags used","Number of observations used", 
                                                        "critical value (1%)", "critical value (5%)", "critical value (10%)"]})
st.write(output_df)


