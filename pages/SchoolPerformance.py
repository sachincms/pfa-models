import streamlit as st
import joblib
import numpy as np
import os
import logging
from pathlib import Path
import base64

current_path = os.path.abspath(__file__)
root_path = os.path.dirname(os.path.dirname(current_path))

CMS_LOGO_PATH = os.path.join(os.getcwd(), 'static', 'images', 'cms_logo.svg')
LOGO_STYLE_PATH = os.path.join(os.getcwd(), 'static', 'html', 'logo_style.html')

model_eng = joblib.load(os.path.join(root_path, 'school_models', 'school_model_eng_ka.pkl'))
model_math = joblib.load(os.path.join(root_path, 'school_models', 'school_model_eng_ka.pkl'))
model_sci = joblib.load(os.path.join(root_path, 'school_models', 'school_model_eng_ka.pkl'))

def img_to_bytes(img_path):
    try:
        img_bytes = Path(img_path).read_bytes()
        encoded = base64.b64encode(img_bytes).decode()
        return encoded
    except Exception as ex:
        logging.error(f'Error in img_to_bytes: {ex}')
        return None

def img_to_html(img_path):
    try:
        img_html = f"<img src='data:image/svg+xml;base64,{img_to_bytes(img_path)}' class='img-fluid' id='fixed-image'>"
        return img_html
    except Exception as ex:
        logging.error(f'Error in img_to_html: {ex}')
        return None

def set_page_configs():
    st.set_page_config(page_title='PFA Predictors', page_icon=CMS_LOGO_PATH, layout="wide")

def main():
    set_page_configs()
    try:
        with open(LOGO_STYLE_PATH) as f:
            st.markdown(f.read(), unsafe_allow_html=True)

        st.markdown(img_to_html(CMS_LOGO_PATH), unsafe_allow_html=True)

    except Exception as ex:
        logging.error(f'Error in display_image_and_intro: {ex}')
        return None
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
        model = model_math
    elif subject == 'Science':
        model = model_sci
    else:
        model = model_eng

    if st.button('Predict'):
        prediction = model.predict(features)[0]
        prediction_proba = model.predict_proba(features)[0]
        
        highest_proba_class = prediction_proba.argmax()
        highest_proba_score = prediction_proba[highest_proba_class]
        
        class_labels = {
            0: 'Considerable improvement',
            1: 'High Improvement',
            2: 'Little Improvement',
            3: 'No Improvement'
        }
        predicted_label = class_labels.get(highest_proba_class, 'Unknown')

        st.write(f'Final Prediction: {predicted_label}')
        st.write(f'Probability of the predicted class: {highest_proba_score:.4f}')

if __name__ == '__main__':
    main()

