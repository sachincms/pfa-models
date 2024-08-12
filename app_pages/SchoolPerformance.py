import streamlit as st
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.getcwd()))
from utils.image_utils import img_to_html
from utils.app_utils import set_page_configs
from config import PFA_LOGO_PATH, CMS_LOGO_PATH, LOGO_STYLE_PATH, PFA_LOGO_STYLE_PATH, SCHOOL_MODEL_ENGLISH, SCHOOL_MODEL_MATH, SCHOOL_MODEL_SCIENCE

def school_performance():
    set_page_configs()
    try:
        with open(PFA_LOGO_STYLE_PATH) as f:
            st.markdown(f.read(), unsafe_allow_html=True)

        st.markdown(img_to_html(PFA_LOGO_PATH, 'png', 'pfa_logo'), unsafe_allow_html=True)

    except Exception as ex:
        print(f'Error displaying logo: {ex}')
        st.markdown('<h2 style="text-align:center; margin-top:5%; margin-bottom:-5%;">Transform Schools</h2>', unsafe_allow_html=True)

    st.markdown('<h2 style="text-align:center; margin-top:5%; margin-bottom:-5%;">School Performance Predictor</h2>', unsafe_allow_html=True)
    st.divider()
    
    col1, col2, _ = st.columns(3)
    with col1:
        st.markdown('<h4 style="text-align:center; color: #64e3b2; margin-bottom:-10%;">Select Subject:</h4>', unsafe_allow_html=True)
    with col2:
        subject = st.selectbox('Select Subject', ['Math', 'Science','English'], label_visibility='collapsed')

    st.markdown('<h5 style="color:#a35edb; text-decoration: underline;">School Location:</h5>', unsafe_allow_html=True)
    col4, _ = st.columns(2)
    rural_urban_option = col4.radio('Rural/Urban', ['Rural', 'Urban'], horizontal=True)
    rural_urban = 0 if rural_urban_option == 'Rural' else 1

    st.markdown('<h5 style="color:#a35edb; text-decoration: underline;">UDISE Indicators:</h5>', unsafe_allow_html=True)
    col6, col7 = st.columns(2)
    with col6:
        school_vigilance = st.slider('School Vigilance', 0.0, 1.0, step=0.1)
        digi_index = st.slider('Digital Index', 0.0, 1.0, step=0.1)
        caste_diversity = st.slider('Caste Diversity', 0.0, 1.0, step=0.1)
        gender_ratio = st.slider('Gender Ratio', 0.0, 1.0, step=0.1)

    with col7:
        economic_diversity = st.slider('Economic Diversity', 0.0, 1.0, step=0.1)
        sanitation_index = st.slider('Sanitation Index', 0.0, 1.0, step=0.1)
        final_teacher_quality = st.slider('Final Teacher Quality', 0.0, 1.0, step=0.1)
        final_numbers_infra = st.slider('Final Numbers Infra', 0.0, 1.0, step=0.1)
    
    features = np.array([[rural_urban, school_vigilance, digi_index, caste_diversity, 
                          gender_ratio, economic_diversity, sanitation_index, 
                          final_teacher_quality, final_numbers_infra]])

    if subject == 'Math':
        model = SCHOOL_MODEL_MATH
    elif subject == 'Science':
        model = SCHOOL_MODEL_SCIENCE
    else:
        model = SCHOOL_MODEL_ENGLISH

    if st.button('Predict'):
        prediction = model.predict(features)[0]
        prediction_proba = model.predict_proba(features)[0]
        
        highest_proba_class = prediction_proba.argmax()
        highest_proba_score = prediction_proba[highest_proba_class]
        probability = np.round(highest_proba_score * 100, 2)
        
        class_labels = {
            0: ['Considerable improvement', 'green'],
            1: ['High Improvement', 'green'],
            2: ['Little Improvement', 'orange'],
            3: ['No Improvement', 'red']
        }
        predicted_label = class_labels.get(highest_proba_class)[0]
        prediction_color = class_labels.get(highest_proba_class)[1]

        st.write(f'Final Prediction: :{prediction_color}[{predicted_label}] ')
        st.write(f'Probability of the predicted class: :{prediction_color}[{probability}%]')
    
    st.markdown('<h6 style="text-align:center;">Powered by</h6>', unsafe_allow_html=True)
    try:
        with open(LOGO_STYLE_PATH) as f:
            st.markdown(f.read(), unsafe_allow_html=True)

        st.markdown(img_to_html(CMS_LOGO_PATH, 'svg', 'cms_logo'), unsafe_allow_html=True)

    except Exception as ex:
        print(f'Error displaying logo: {ex}')
        st.markdown('<h2 style="text-align:center; margin-top:5%; margin-bottom:-5%;">Catalyst Management Services</h2>', unsafe_allow_html=True)