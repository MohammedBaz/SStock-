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
Title=np.array(['Max Opening Price','Max Opening Date','Max Closing Price','Max Closing Date',
       'Max Highest Price','Max Highest Date','Max Lowest Price','Max Lowest Date',
       'Max Volume_traded Price','Max Volume_traded Date','Max No_trades Price','Max No_trades Price Date',
       'Max Value_traded Price','Max Value_traded Date'], dtype=object)
Values=np.array([df1['open'][df1['open'].idxmax()],df1['date1'][df1['open'].idxmax()],
                df1['close'][df1['close'].idxmax()],df1['date1'][df1['close'].idxmax()],
                df1['high'][df1['high'].idxmax()],df1['date1'][df1['high'].idxmax()],
                df1['low'][df1['low'].idxmax()],df1['date1'][df1['high'].idxmax()],
                df1['volume_traded '][df1['volume_traded '].idxmax()],df1['date1'][df1['volume_traded '].idxmax()],
                df1['no_trades '][df1['no_trades '].idxmax()],df1['date1'][df1['no_trades '].idxmax()],
                df1['value_traded'][df1['value_traded'].idxmax()], df1['date1'][df1['value_traded'].idxmax()]
                 ], dtype=object)
dataset = pd.DataFrame()
dataset['Title'] = Title
dataset['Values'] = Values
st.write(dataset)




#chart_data = df1[['open','high','low','close','volume_traded ','no_trades ','value_traded']].copy()
#dchart_data = pd.DataFrame(chart_data.describe(include='all'))
#st.dataframe(dchart_data)  # Same as st.write(df)
#st.write('One day Autocorrelation',chart_data['open'].autocorr(lag=1))
#st.write('One week Autocorrelation',chart_data['open'].autocorr(lag=7))
#st.write('One month Autocorrelation',chart_data['open'].autocorr(lag=30))
#st.write('One year Autocorrelation',chart_data['open'].autocorr(lag=365))


