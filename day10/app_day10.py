import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green', 'Orange', 'Yellow', 'Black', 'Pink'))

style = f'<p style="font-family:sans-serif; color:{option}; font-size: 30px;">Your favorite color is {option}</p>'

st.markdown(style, unsafe_allow_html=True)
