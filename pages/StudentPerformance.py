import streamlit as st
import joblib
import numpy as np
from pathlib import Path
import base64
import os

STUDENT_MODEL_ENG = joblib.load(os.path.join('student_models', 'logistic_regression_model_eng.pkl'))
STUDENT_MODEL_MATH = joblib.load(os.path.join('student_models', 'logistic_regression_model_math.pkl'))
STUDENT_MODEL_SCIENCE = joblib.load(os.path.join('student_models', 'logistic_regression_model_sci.pkl'))

CMS_LOGO_PATH = os.path.join(os.getcwd(), 'static', 'images', 'cms_logo.svg')
LOGO_STYLE_PATH = os.path.join(os.getcwd(), 'static', 'html', 'logo_style.html')

def img_to_bytes(img_path):
    try:
        img_bytes = Path(img_path).read_bytes()
        encoded = base64.b64encode(img_bytes).decode()
        return encoded
    except Exception as ex:
        print(f'Error in img_to_bytes: {ex}')
        return None

def img_to_html(img_path):
    try:
        img_html = f"<img src='data:image/svg+xml;base64,{img_to_bytes(img_path)}' class='img-fluid' id='fixed-image'>"
        return img_html
    except Exception as ex:
        print(f'Error in img_to_html: {ex}')
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
        print(f'Error in display_image_and_intro: {ex}')
        return None

    st.markdown('<h2 style="text-align:center; margin-top:5%; margin-bottom:-5%;">Student Performance Predictor</h2>', unsafe_allow_html=True)
    st.divider()

    # st.markdown('''
    #         <style>

    #             /* Value above slider */
    #             div[data-testid="stThumbValue"]{
    #                 color:#64e3b2;
    #             }

    #             /* Slider head */
    #             div.stSlider > div[data-baseweb="slider"] > div > div > div[role="slider"]{
    #                 background-color: #64e3b2;
    #                 box-shadow: #64e3b2 
    #             }

    #             /* Slider track */
    #             div.stSlider > div[data-baseweb = "slider"] > div > div[class="class="st-ds st-c5 st-c7 st-c6 st-as st-ct st-dt"] {
    #                 background: linear-gradient(
    #                             to right, 
    #                             rgb(100, 227, 178) 0%, 
    #                             rgb(100, 227, 178) 25%, 
    #                             rgba(100, 227, 178, 0.25) 50%,
    #                             rgba(100, 227, 178, 0.25) 75%,
    #                             rgba(100, 227, 178, 0.25) 100%
    #                 );
    #             }

    #             /* Slider Min Max Values */

    #             div.stSlider > div[data-baseweb = "slider"] > div[data-testid="stTickBar"] > div {
    #                 background: rgb(100, 227, 178); 
    #             }

    #             /* Radio button */
    #             div.stRadio > label[data-baseweb="radio"] > div[class="st-dg st-d6 st-d7 st-d8 st-d9 st-dh st-b4 st-b5 st-di"]{
    #                 background-color: #64e3b2;
    #                 background: #64e3b2;
    #             }

    #         </style>
    #     ''', unsafe_allow_html=True)

    col1, col2, _ = st.columns(3)
    
    with col1:
        st.markdown('<h4 style="text-align:center; color: #64e3b2; margin-bottom:-10%;">Select Subject:</h4>', unsafe_allow_html=True)
    with col2:
        subject = st.selectbox('Select Subject', ['Math', 'Science','English'], label_visibility='collapsed')
    
    st.markdown('<h5 style="color:#a35edb; text-decoration: underline;">Student Information:</h5>', unsafe_allow_html=True)

    col4, col5 = st.columns(2)
    gender_option = col4.radio('Gender', ['Male', 'Female'], horizontal=True)
    gender = 0 if gender_option == 'Female' else 1
    bl_level = col5.slider('Baseline Level (values from 1 to 5)', 1, 5)

    st.markdown('<h5 style="color:#a35edb; text-decoration: underline;">Competencies:</h5>', unsafe_allow_html=True)

    col6, col7 = st.columns(2)
    if subject == 'Math':
        model = STUDENT_MODEL_MATH

        with col6:
            arithmetic_and_number_operations = st.slider('Arithmetic and Number Operations', 0.0, 1.0, step=0.05)
            geometrical_ideas = st.slider('Geometrical Ideas', 0.0, 1.0, step=0.05)
            data_handling_and_statistics = st.slider('Data Handling and Statistics', 0.0, 1.0, step=0.05)
        
        with col7:
            algebra_and_mathematical_reasoning = st.slider('Algebra and Mathematical Reasoning', 0.0, 1.0, step=0.05)
            measurement = st.slider('Measurement', 0.0, 1.0, step=0.05)
            problem_solving_and_real_life_applications = st.slider('Problem Solving and Real Life Applications', 0.0, 1.0, step=0.05)

        features = np.array([[arithmetic_and_number_operations, geometrical_ideas,
                              data_handling_and_statistics, algebra_and_mathematical_reasoning,
                              measurement, problem_solving_and_real_life_applications, bl_level, gender]])
        
    elif subject == 'Science':
        model = STUDENT_MODEL_SCIENCE

        with col6:
            understanding_and_analysis = st.slider('Understanding and Analysis', 0.0, 1.0, step=0.05)
            identification_and_classification = st.slider('Identification and Classification', 0.0, 1.0, step=0.05)
            recall_and_memory = st.slider('Recall and Memory', 0.0, 1.0, step=0.05)
        
        with col7:
            understanding_properties_and_functions = st.slider('Understanding Properties and Functions', 0.0, 1.0, step=0.05)
            measurement_and_conversion = st.slider('Measurement and Conversion', 0.0, 1.0, step=0.05)
            application_of_concepts = st.slider('Application of Concepts', 0.0, 1.0, step=0.05)
        
        features = np.array([[understanding_and_analysis, identification_and_classification,
                              recall_and_memory, understanding_properties_and_functions,
                              measurement_and_conversion, application_of_concepts, bl_level, gender]])
        
    else:
        model = STUDENT_MODEL_ENG

        with col6:
            language_structure_and_grammar = st.slider('Language Structure and Grammar', 0.0, 1.0, step=0.05)
            vocabulary_and_word_usage = st.slider('Vocabulary and Word Usage', 0.0, 1.0, step=0.05)
            reading_and_comprehension = st.slider('Reading and Comprehension', 0.0, 1.0, step=0.05)
        
        with col7:
            writing_and_composition = st.slider('Writing and Composition', 0.0, 1.0, step=0.05)
            contextual_and_functional_use_of_language = st.slider('Contextual and Functional Use of Language', 0.0, 1.0, step=0.05)
        
        features = np.array([[language_structure_and_grammar, vocabulary_and_word_usage,
                              reading_and_comprehension, writing_and_composition,
                              contextual_and_functional_use_of_language, bl_level, gender]])

    if st.button('Predict'):
        prediction = model.predict(features)[0]
        prediction_color = 'green' if prediction == 1 else 'red'
        prediction_message = 'Student is likely to pass' if prediction == 1 else 'Student is likely to fail'
        prediction_proba = model.predict_proba(features)[0, 1]  # Probability of the output being 1
        probability = np.round(prediction_proba * 100, 2)
        
        st.write(f'Final Prediction: :{prediction_color}[{prediction_message}]')
        st.write(f'Probability of student passing: :{prediction_color}[{probability}%]')

# if __name__ == '__main__':
#     main()