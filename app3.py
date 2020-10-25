import streamlit as st

def app():

    st.write('# Quarantine Trends')

    col1, col2 = st.beta_columns(2)

    with col1:
        st.header("Time at Home")

    with col2:
        st.header("New COVID-19 Cases")

    st.image("https://blueprintdata2020.s3-us-west-1.amazonaws.com/1.png", use_column_width = True, output_format = 'JPEG')
    st.image("https://blueprintdata2020.s3-us-west-1.amazonaws.com/2.png", use_column_width = True, output_format = 'JPEG')
    st.image("https://blueprintdata2020.s3-us-west-1.amazonaws.com/3.png", use_column_width = True, output_format = 'JPEG')
    st.image("https://blueprintdata2020.s3-us-west-1.amazonaws.com/4.png", use_column_width = True, output_format = 'JPEG')
    st.image("https://blueprintdata2020.s3-us-west-1.amazonaws.com/5.png", use_column_width = True, output_format = 'JPEG')
    st.image("https://blueprintdata2020.s3-us-west-1.amazonaws.com/6.png", use_column_width = True, output_format = 'JPEG')
    st.image("https://blueprintdata2020.s3-us-west-1.amazonaws.com/7.png", use_column_width = True, output_format = 'JPEG')
    st.image("https://blueprintdata2020.s3-us-west-1.amazonaws.com/8.png", use_column_width = True, output_format = 'JPEG')
    st.image("https://blueprintdata2020.s3-us-west-1.amazonaws.com/9.png", use_column_width = True, output_format = 'JPEG')
    st.image("https://blueprintdata2020.s3-us-west-1.amazonaws.com/10.png", use_column_width = True, output_format = 'JPEG')
    st.image("https://blueprintdata2020.s3-us-west-1.amazonaws.com/11.png", use_column_width = True, output_format = 'JPEG')