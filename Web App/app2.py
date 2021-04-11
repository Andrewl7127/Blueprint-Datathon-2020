import streamlit as st

def app():

    st.write('# Demographics')

    st.write('### Proportion of Single Residents')
    st.markdown("![Alt Text](https://blueprintdata2020.s3-us-west-1.amazonaws.com/single.PNG)")

    st.write('### Proportion of Asian Residents')
    st.markdown("![Alt Text](https://blueprintdata2020.s3-us-west-1.amazonaws.com/asian.PNG)")

    st.write('### Proportion of Black Residents')
    st.markdown("![Alt Text](https://blueprintdata2020.s3-us-west-1.amazonaws.com/black.PNG)")

    st.write('### Proportion of White Residents')
    st.markdown("![Alt Text](https://blueprintdata2020.s3-us-west-1.amazonaws.com/white.PNG)")
