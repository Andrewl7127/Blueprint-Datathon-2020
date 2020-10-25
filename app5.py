import streamlit as st

def app():

    st.write('# Random Forest Models')

    st.write('## Base Model')
    st.image("https://blueprintdata2020.s3-us-west-1.amazonaws.com/default.PNG", use_column_width = True, output_format = 'JPEG')

    st.write('## Best RandomSearchCV Model')
    st.image("https://blueprintdata2020.s3-us-west-1.amazonaws.com/random.PNG", use_column_width = True, output_format = 'JPEG')

    st.write('## Best GridSearchCV Model')
    st.image("https://blueprintdata2020.s3-us-west-1.amazonaws.com/grid.PNG", use_column_width = True, output_format = 'JPEG')

    