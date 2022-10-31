import streamlit as st
import pandas as pd
import numpy as np




df = pd.read_csv('out.csv')
df["date1"] = pd.to_datetime(df["date1"]) 
df =df.sort_values(by='date1')

option = st.selectbox('Select the Compmay name',df['name'].unique())
df1=df.loc[df['name'] == option]

X1=['open',	'high',	'low',	'close','volume_traded ','value_traded','no_trades ']



from statsmodels.tsa.stattools import adfuller
adft = adfuller(df1['open'],autolag="AIC")
output_df = pd.DataFrame({"Values":[adft[0],adft[1],adft[2],adft[3], adft[4]['1%'], adft[4]['5%'], adft[4]['10%']]  , "Metric":["Test Statistics","p-value","No. of lags used","Number of observations used", 
                                                        "critical value (1%)", "critical value (5%)", "critical value (10%)"]})
st.write(output_df)

adft = adfuller(df1['high'],autolag="AIC")
output_df = pd.DataFrame({"Values":[adft[0],adft[1],adft[2],adft[3], adft[4]['1%'], adft[4]['5%'], adft[4]['10%']]  , "Metric":["Test Statistics","p-value","No. of lags used","Number of observations used", 
                                                        "critical value (1%)", "critical value (5%)", "critical value (10%)"]})
st.write(output_df)

adft = adfuller(df1['low'],autolag="AIC")
output_df = pd.DataFrame({"Values":[adft[0],adft[1],adft[2],adft[3], adft[4]['1%'], adft[4]['5%'], adft[4]['10%']]  , "Metric":["Test Statistics","p-value","No. of lags used","Number of observations used", 
                                                        "critical value (1%)", "critical value (5%)", "critical value (10%)"]})
st.write(output_df)

adft = adfuller(df1['close'],autolag="AIC")
output_df = pd.DataFrame({"Values":[adft[0],adft[1],adft[2],adft[3], adft[4]['1%'], adft[4]['5%'], adft[4]['10%']]  , "Metric":["Test Statistics","p-value","No. of lags used","Number of observations used", 
                                                        "critical value (1%)", "critical value (5%)", "critical value (10%)"]})
st.write(output_df)

