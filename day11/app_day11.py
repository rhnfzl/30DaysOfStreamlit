import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue', 'Pink', 'Olive', 'Orange'],
     ['Yellow', 'Red'])

color_options = list()
if options:
    for i in options:
        color_options.append(f'<p style="font-family:sans-serif; color:{i}; font-size: 14px;">{i}</p>')

st.markdown(color_options, unsafe_allow_html=True)
