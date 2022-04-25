import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(100, 3),
     columns=['a', 'b', 'c'],
     index=pd.date_range("2021-09-10", periods=100, freq="M"))

st.line_chart(chart_data)
