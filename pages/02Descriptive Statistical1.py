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
#df.index =df['date1']
#del df['date1']
option = st.selectbox('Select the Compmay name',df['name'].unique())
df1=df.loc[df['name'] == option]


fig, ax = plt.subplots(1, 2)

#create chart in each subplot
sns.lineplot(data=df1, x="date1", y="open");ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
sns.lineplot(data=df1, x="date1", y="close");ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
st.pyplot(plt)


#fig, ax = plt.subplots()
#ax= sns.lineplot(data=df1, x="date1", y="open");ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
#ax1= sns.lineplot(data=df1, x="date1", y="close");ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
#ax2= sns.lineplot(data=df1, x="date1", y="high");ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
#ax3= sns.lineplot(data=df1, x="date1", y="low");ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
#st.pyplot(plt)
#ax1 = sns.lineplot(x='x', y='z', data=data)



#ax=sns.lineplot(data=df1, x="date1", y="open")
#ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
#plt.ylabel("Opening Price")
#st.pyplot(plt)



#fig, axes = plt.subplots(nrows=2, ncols=2)
#plt.plot(df.date1, df.open, linewidth=3,)
#sns.lineplot(df)
#df1['date1','open'].plot(ax=axes[0,0]); axes[0,0].set_title('Opening Price')
#df1['open'].plot(ax=axes[0,0]); axes[0,0].set_title('Opening Price')
#df1['close'].plot(ax=axes[0,1]); axes[0,1].set_title('Closing Price')
#df1['high'].plot(ax=axes[1,0]); axes[1,0].set_title('high Price')
#df1['low'].plot(ax=axes[1,1]); axes[1,1].set_title('low Price')
#st.pyplot(plt)
#df1 = df1.rename(columns={'date1':'index'}).set_index('index')

#plt.plot(df.x, df.y)

#df1.set_index('date1')
#chart_data = df1[['open','high','low','close','volume_traded ','no_trades ','value_traded','date1']].copy()
#chart_data.set_index('date1')
#plt.figure()
#chart_data.plot(subplots=True, figsize=(6, 6))
#plt.legend(loc='best');plt.xticks(rotation=90) # for more plot option see https://pandas.pydata.org/pandas-docs/version/0.13/visualization.html
#st.pyplot(plt)
