# Contents of ~/my_app/main_page.py
import streamlit as st
import pandas as pd

st.markdown("#This project was created for research purposes. It is not intended to be used as recommendations system and we disclaim any responsibility for any misuse of it 🎈")
st.sidebar.markdown("# Main page 🎈")
df = pd.read_csv('out.csv')
st.dataframe(df)
