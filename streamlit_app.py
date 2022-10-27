# Contents of ~/my_app/main_page.py
import streamlit as st

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")
df = pd.read_csv('Tadawul_stcks_23_4.csv')
st.dataframe(df)
