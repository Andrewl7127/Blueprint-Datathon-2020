import streamlit as st

def app():

    st.write('# About Us')

    col1, col2 = st.beta_columns(2)

    with col1:
        st.header("Kyle Fang")
        st.image("https://blueprintdata2020.s3-us-west-1.amazonaws.com/kyle.jpg", use_column_width = True, output_format = 'JPEG', caption ='''
        Kyle is an undergraduate student at the University of California, Los Angeles (UCLA) majoring in Applied Mathematics with a minor in Statistics ('22).''')

    with col2:
        st.header("William Foote")
        st.image("https://blueprintdata2020.s3-us-west-1.amazonaws.com/will.jpg", use_column_width = True, output_format = 'JPEG', caption ='''
        William is an undergraduate student at the University of California, Los Angeles (UCLA) majoring in Statistics ('21).''')

    col3, col4 = st.beta_columns(2)

    with col3:
        st.header("Andrew Liu")
        st.image("https://raw.githubusercontent.com/shailm99/TAMU-Datathon-2020/main/andrew.png", use_column_width = True, output_format = 'JPEG', caption ='''
        Andrew is an undergraduate student at the University of California, Los Angeles (UCLA) majoring in Data Theory ('23).''')

    with col4:
        st.header("Adhvaith Vijay")
        st.image("https://raw.githubusercontent.com/shailm99/TAMU-Datathon-2020/main/adhvaith.jpg", use_column_width = True, output_format = 'JPEG', caption ='''
        Adhvaith is an undergraduate student at the University of California, Los Angeles (UCLA) majoring in Data Theory ('22).''')
