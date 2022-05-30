import streamlit as st

st.write('This is a title')

food = ['Aloo Patty', 'Veg Roll', 'Cold Coffee', 'Paneer Patty']
options = st.multiselect(
     'What you want to eat at arts faculty ?',
     food)

st.write('You selected:', options)
