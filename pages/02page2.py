# Contents of ~/my_app/pages/page_2.py
# the (02) prefix of 02page2.py has been added to ensure the correct sort of pages only 
import streamlit as st
df = pd.read_csv('out.csv')
option = st.selectbox('Select the Compmay name',df['name'].unique())
