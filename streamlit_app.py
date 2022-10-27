# Contents of ~/my_app/main_page.py
import streamlit as st
import pandas as pd

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")
df = pd.read_csv('out.csv')
st.dataframe(df)
