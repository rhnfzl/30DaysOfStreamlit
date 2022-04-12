import streamlit as st

st.header('st.checkbox')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
chai = st.checkbox('Chai')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")

if chai:
     st.write("Okay, here's some Chai ☕")

if cola:
     st.write("Here you go 🥤")
