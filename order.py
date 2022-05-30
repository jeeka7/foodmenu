import streamlit as st

st.title('This is a title')

food = ['Green', 'Yellow', 'Red', 'Blue']
options = st.multiselect(
     'What you want to eat at arts faculty ?',
     food)

st.write('You selected:', options)
