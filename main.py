import streamlit as st
from datetime import datetime 

st.title('Hello world')

st.write('test')
st.write('update')

d = st.date_input("転職予定日", datetime.date(2021,6,1))
st.write(d)
