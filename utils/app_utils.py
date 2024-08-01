import streamlit as st
from config import CMS_LOGO_PATH

def set_page_configs():
    st.set_page_config(page_title='PFA Predictors', page_icon=CMS_LOGO_PATH, layout="wide")