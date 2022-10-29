import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
import seaborn as sns

df = pd.read_csv('out.csv')
df["date1"] = pd.to_datetime(df["date1"]) 
df =df.sort_values(by='date1')
df.index = df['date1']


SelectedName = st.multiselect('Select the Compmay name',df['name'].unique())

def GenerateCrossCorrMat():
  SelectedList=[]
  ans=np.empty((len(SelectedName),len(SelectedName)), dtype=object)
  #ans[0,1:]=SelectedName
  #ans[1:,0]=SelectedName
  for i in range(len(SelectedName)):
    SelectedList.append([])
    SelectedList[i]=df['open'].loc[df['name'] == SelectedName[i]]

  for i in range (len(SelectedName)):
    for j in range (len(SelectedName)):
      print(i,j,SelectedList[i].corr(SelectedList[j]))
      ans[i,j]=SelectedList[i].corr(SelectedList[j])
  return (ans)

ans=GenerateCrossCorrMat()
dfans=pd.DataFrame(ans)
dfans.columns = SelectedName
dfans.index = SelectedName
st.write(dfans)
