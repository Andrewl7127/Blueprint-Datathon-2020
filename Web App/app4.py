import streamlit as st

def app():

    st.write('# Policy Trends')

    col1, col2 = st.beta_columns(2)

    with col1:
        st.image("https://blueprintdata2020.s3-us-west-1.amazonaws.com/jan.png", use_column_width = True, output_format = 'JPEG', caption = 'January')

    with col2:
        st.image("https://blueprintdata2020.s3-us-west-1.amazonaws.com/feb.png", use_column_width = True, output_format = 'JPEG', caption ='February')

    col3, col4 = st.beta_columns(2)

    with col3:
        st.image("https://blueprintdata2020.s3-us-west-1.amazonaws.com/mar.png", use_column_width = True, output_format = 'JPEG', caption ='March')

    with col4:
        st.image("https://blueprintdata2020.s3-us-west-1.amazonaws.com/apr.png", use_column_width = True, output_format = 'JPEG', caption ='April')

    col5, col6 = st.beta_columns(2)

    with col5:
        st.image("https://blueprintdata2020.s3-us-west-1.amazonaws.com/may.png", use_column_width = True, output_format = 'JPEG', caption ='May')

    with col6:
        st.image("https://blueprintdata2020.s3-us-west-1.amazonaws.com/jun.png", use_column_width = True, output_format = 'JPEG', caption ='June')

    col7, col8 = st.beta_columns(2)

    with col7:
        st.image("https://blueprintdata2020.s3-us-west-1.amazonaws.com/jul.png", use_column_width = True, output_format = 'JPEG', caption ='July')

    with col8:
        st.image("https://blueprintdata2020.s3-us-west-1.amazonaws.com/aug.png", use_column_width = True, output_format = 'JPEG', caption ='August')

    col9, col10 = st.beta_columns(2)

    with col9:
        st.image("https://blueprintdata2020.s3-us-west-1.amazonaws.com/sep.png", use_column_width = True, output_format = 'JPEG', caption ='September')

    with col10:
        st.image("https://blueprintdata2020.s3-us-west-1.amazonaws.com/oct.png", use_column_width = True, output_format = 'JPEG', caption ='October')
