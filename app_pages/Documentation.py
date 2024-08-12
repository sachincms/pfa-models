import streamlit as st
import os
import sys
sys.path.append(os.path.dirname(os.getcwd()))
from utils.app_utils import set_page_configs
from utils.image_utils import img_to_html
from config import DOCUMENTATION_PATH, PFA_LOGO_PATH, PFA_LOGO_STYLE_PATH

def documentation():
    set_page_configs()
    try:
        with open(PFA_LOGO_STYLE_PATH) as f:
            st.markdown(f.read(), unsafe_allow_html=True)

        st.markdown(img_to_html(PFA_LOGO_PATH, 'png', 'pfa_logo'), unsafe_allow_html=True)

    except Exception as ex:
        print(f'Error displaying logo: {ex}')
        st.markdown('<h2 style="text-align:center; margin-top:5%; margin-bottom:-5%;">Transform Schools</h2>', unsafe_allow_html=True)

    st.markdown('<h2 style="text-align:center; margin-top:0%; margin-bottom:-5%;"></h2>', unsafe_allow_html=True)
    st.divider()

    try:
        with open(DOCUMENTATION_PATH) as f:
            st.markdown(f.read(), unsafe_allow_html=True)
    except Exception as ex:
        print(f'Error displaying documentation: {ex}')
        st.markdown('<h2 style="text-align:center; margin-top:5%; margin-bottom:-5%;">Documentation</h2>', unsafe_allow_html=True)
    