import streamlit as st
import keras
import numpy as np
from tensorflow.keras.models import load_model
model = load_model('modelx.h5')
st.write(model.summary())
