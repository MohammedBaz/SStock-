import streamlit as st
import keras
import numpy as np
from tensorflow.keras.models import load_model
model = load_model('modelx.h5')


import numpy as np
import pandas as pd

df = pd.read_csv("tasi_d.csv")
df['Date'] =pd.to_datetime(df['Date'])
df=df.sort_values(by=['Date'])
df.set_index('Date',inplace=True, drop=True)
df['Open'] = df['Open'].astype(float)
df['High'] = df['High'].astype(float)
df['Low'] = df['Low'].astype(float)
df['Close'] = df['Close'].astype(float)
df['Volume'] = df['Volume'].astype(float)

def ReshapeArrayTimeStepY(Inputarray,TimeStep):
  OutputArray=np.empty([len(Inputarray)-TimeStep,])
  for i in range(len(Inputarray)-TimeStep):
    OutputArray[i]=Inputarray[i+TimeStep]
  OutputArray=OutputArray.reshape(len(OutputArray),1)
  return OutputArray

def ReshapeArrayTimeStepX(Inputarray,TimeStep):
  OutputArray=np.empty([len(Inputarray)-TimeStep,TimeStep])
  for i in range(len(Inputarray)-TimeStep):
    OutputArray[i,:]=Inputarray[i:i+TimeStep]
  OutputArray=OutputArray.reshape(len(OutputArray),TimeStep,1)
  return OutputArray

NodeNumber=500
NumberofTimesteps=1

x=ReshapeArrayTimeStepX (df['Close'].tail(100),1)
y=ReshapeArrayTimeStepY (df['Close'].tail(100),1)

x_input = np.array([y[-NumberofTimesteps-1:-1]]).reshape((1, NumberofTimesteps, 1))
prediction = model.predict(x_input) 
st.write(prediction)
