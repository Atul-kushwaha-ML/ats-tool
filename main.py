
import streamlit as st
from home import render_home
from analyzer import render_analyzer

st.set_page_config(
    page_title="AI ATS Analyzer",
    page_icon="🎯",
    layout="centered"
)

if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    render_home()
else:
    render_analyzer()