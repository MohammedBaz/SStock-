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


fig, (ax1, ax2,ax3, ax4,ax5, ax6,ax7) = plt.subplots( )


ax1= sns.lineplot(data=df1, x="date1", y="open")
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=40, ha="right")
ax1.set_xlabel('Date')  
ax1.yaxis.set_label_text('Opening price')
st.pyplot(fig)

ax2= sns.lineplot(data=df1, x="date1", y="close")
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=40, ha="right")
ax2.set_xlabel('Date')  
ax2.yaxis.set_label_text('Closing price')
st.pyplot(fig)

ax3= sns.lineplot(data=df1, x="date1", y="high")
ax3.set_xticklabels(ax3.get_xticklabels(), rotation=40, ha="right")
ax3.set_xlabel('Date')  
ax3.yaxis.set_label_text('Highest price')
st.pyplot(fig)

ax4= sns.lineplot(data=df1, x="date1", y="low")
ax4.set_xticklabels(ax4.get_xticklabels(), rotation=40, ha="right")
ax4.set_xlabel('Date')    
ax4.yaxis.set_label_text('Lowest price')
st.pyplot(fig)

ax5= sns.lineplot(data=df1, x="date1", y="volume_traded ")
ax5.set_xticklabels(ax5.get_xticklabels(), rotation=40, ha="right")
ax5.set_xlabel('Date')   
ax5.yaxis.set_label_text('Traded Volume')
st.pyplot(fig)

ax6= sns.lineplot(data=df1, x="date1", y="no_trades ")
ax6.set_xticklabels(ax6.get_xticklabels(), rotation=40, ha="right")
ax6.set_xlabel('Date')   
ax6.yaxis.set_label_text('Number of Trades')
st.pyplot(fig)

ax7= sns.lineplot(data=df1, x="date1", y="value_traded")
ax7.set_xticklabels(ax7.get_xticklabels(), rotation=40, ha="right")
ax7.set_xlabel('Date')    
ax7.yaxis.set_label_text('Trading price')
st.pyplot(fig)

