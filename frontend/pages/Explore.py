import streamlit as st
import pandas as pd
from io import StringIO
import altair as alt

uploaded_file = st.file_uploader("Choose a csv file")
if uploaded_file is not None:
    chart_data = pd.read_csv(uploaded_file)
    x_axis = chart_data.columns[0]
    y_axis = chart_data.columns[1]
    color = chart_data.columns[2]
    
    st.write("Dataframe:")
    st.write(chart_data)
    
    
    chart = (
        alt.Chart(chart_data)
        .mark_circle()
        .encode(x=x_axis, y=y_axis, color=color, tooltip=[x_axis, y_axis, color])
    )
    st.write("Plot:")
    st.altair_chart(chart, use_container_width=True)