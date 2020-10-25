import app1
import app2
import app3
import app4
import app5
import app6
import app7
import streamlit as st
import streamlit_theme as stt

stt.set_theme({'primary': '#FF1493'})

PAGES = {
    "COVID-19 Trends": app1,
    "Demographics": app2,
    "Quarantine Trends": app3,
    "Policy Trends": app4,
    "Random Forest Models": app5,
    "About Us": app6,
    "The Task": app7,
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()