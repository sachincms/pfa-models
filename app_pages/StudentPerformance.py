import streamlit as st
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.getcwd()))
from utils.image_utils import img_to_html
from utils.app_utils import set_page_configs
from config import *

def student_performance():
    set_page_configs()
    
    try:
        with open(PFA_LOGO_STYLE_PATH) as f:
            st.markdown(f.read(), unsafe_allow_html=True)

        st.markdown(img_to_html(PFA_LOGO_PATH, 'png', 'pfa_logo'), unsafe_allow_html=True)

    except Exception as ex:
        print(f'Error displaying logo: {ex}')
        st.markdown('<h2 style="text-align:center; margin-top:5%; margin-bottom:-5%;">Transform Schools</h2>', unsafe_allow_html=True)

    st.markdown('<h2 style="text-align:center; margin-top:5%; margin-bottom:-5%;">Student Performance Predictor</h2>', unsafe_allow_html=True)
    st.divider()

    col1, col2, _ = st.columns(3)
    
    with col1:
        st.markdown('<h4 style="text-align:center; color: #64e3b2; margin-bottom:-10%;">Select Subject:</h4>', unsafe_allow_html=True)
    with col2:
        subject = st.selectbox('Select Subject', ['Math', 'Science','English'], label_visibility='collapsed')
    
    st.markdown('<h5 style="color:#a35edb; text-decoration: underline;">Student Information:</h5>', unsafe_allow_html=True)

    col4, col5, col6 = st.columns(3)
    gender_option = col4.radio('Gender', ['Male', 'Female'], horizontal=True)
    state_option = col5.radio('State', ['Karnataka', 'Odisha'], horizontal=True)
    bl_level = col6.slider('Baseline Level (values from 1 to 5)', 1, 5)

    st.markdown('<h5 style="color:#a35edb; text-decoration: underline;">Competencies:</h5>', unsafe_allow_html=True)

    gender = 0 if gender_option == 'Female' else 1

    col7, col8 = st.columns(2)
    if subject == 'Math':
        if state_option == 'Karnataka':
            model = STUDENT_MODEL_MATH_KARNATAKA
        else:
            model = STUDENT_MODEL_MATH_ODISHA

        with col7:
            arithmetic_and_number_operations = st.slider('Arithmetic and Number Operations', 0.0, 1.0, 0.05)
            geometrical_ideas = st.slider('Geometrical Ideas', 0.0, 1.0, 0.05)
            data_handling_and_statistics = st.slider('Data Handling and Statistics', 0.0, 1.0, 0.05)
        
        with col8:
            algebra_and_mathematical_reasoning = st.slider('Algebra and Mathematical Reasoning', 0.0, 1.0, step=0.05)
            measurement = st.slider('Measurement', 0.0, 1.0, step=0.05)
            problem_solving_and_real_life_applications = st.slider('Problem Solving and Real Life Applications', 0.0, 1.0, step=0.05)

        features = np.array([
            [
                arithmetic_and_number_operations,
                geometrical_ideas,
                data_handling_and_statistics,
                algebra_and_mathematical_reasoning,
                problem_solving_and_real_life_applications,
                measurement,
                bl_level,
                gender
            ]
        ])
        
    elif subject == 'Science':
        if state_option == 'Karnataka':
            model = STUDENT_MODEL_SCIENCE_KARNATAKA

            with col7:
                identification_and_classification = st.slider('Identification and Classification', 0.0, 1.0, step=0.05)
                understanding_describing_processes = st.slider('Understanding and Describing Processes', 0.0, 1.0, step=0.05)
                recall_application = st.slider('Recall and Application', 0.0, 1.0, step=0.05)
            
            with col8:
                work_and_skills = st.slider('Work and Skills', 0.0, 1.0, step=0.05)
                measurement_estimation = st.slider('Measurement and Estimation', 0.0, 1.0, step=0.05)
                science_in_daily_life = st.slider('Science in Daily Life', 0.0, 1.0, step=0.05)

            features = np.array([
                [
                    identification_and_classification, 
                    understanding_describing_processes,
                    work_and_skills,
                    measurement_estimation,
                    science_in_daily_life,
                    recall_application, 
                    bl_level, 
                    gender
                ]
            ])

        else:
            model = STUDENT_MODEL_SCIENCE_ODISHA
            with col7:
                understanding_and_analysis = st.slider('Understanding and Analysis', 0.0, 1.0, step=0.05)
                identification_and_classification = st.slider('Identification and Classification', 0.0, 1.0, step=0.05)
                recall_and_memory = st.slider('Recall and Memory', 0.0, 1.0, step=0.05)
            
            with col8:
                understanding_properties_and_functions = st.slider('Understanding Properties and Functions', 0.0, 1.0, step=0.05)
                measurement_and_conversion = st.slider('Measurement and Conversion', 0.0, 1.0, step=0.05)
                application_of_concepts = st.slider('Application of Concepts', 0.0, 1.0, step=0.05)

            features = np.array([
                [
                    understanding_and_analysis,
                    identification_and_classification,
                    recall_and_memory,
                    understanding_properties_and_functions,
                    measurement_and_conversion,
                    application_of_concepts,
                    bl_level, 
                    gender
                ]
            ])
        
    else:
        if state_option == 'Karnataka':
            model = STUDENT_MODEL_ENGLISH_KARNATAKA
            with col7:
                language_structure_and_grammar = st.slider('Language Structure and Grammar', 0.0, 1.0, step=0.05)
                vocabulary_and_word_usage = st.slider('Vocabulary and Word Usage', 0.0, 1.0, step=0.05)
                reading_and_comprehension = st.slider('Reading and Comprehension', 0.0, 1.0, step=0.05)
            
            with col8:
                writing_and_composition = st.slider('Writing and Composition', 0.0, 1.0, step=0.05)
                contextual_and_functional_use_of_language = st.slider('Contextual and Functional Use of Language', 0.0, 1.0, step=0.05)
                understanding_literature = st.slider('Understanding Literature', 0.0, 1.0, step=0.05)
            
            features = np.array([
                [
                    language_structure_and_grammar, 
                    vocabulary_and_word_usage,
                    reading_and_comprehension,
                    writing_and_composition,
                    contextual_and_functional_use_of_language,
                    understanding_literature,
                    bl_level,
                    gender
                ]
            ])

        else:
            model = STUDENT_MODEL_ENGLISH_ODISHA

            with col7:
                language_structure_and_grammar = st.slider('Language Structure and Grammar', 0.0, 1.0, step=0.05)
                vocabulary_and_word_usage = st.slider('Vocabulary and Word Usage', 0.0, 1.0, step=0.05)
                reading_and_comprehension = st.slider('Reading and Comprehension', 0.0, 1.0, step=0.05)
            
            with col8:
                writing_and_composition = st.slider('Writing and Composition', 0.0, 1.0, step=0.05)
                contextual_and_functional_use_of_language = st.slider('Contextual and Functional Use of Language', 0.0, 1.0, step=0.05)
            
            features = np.array([
                [
                    language_structure_and_grammar, 
                    vocabulary_and_word_usage,
                    reading_and_comprehension,
                    writing_and_composition,
                    contextual_and_functional_use_of_language,
                    bl_level,
                    gender
                ]
            ])

    if st.button('Predict'):
        prediction = model.predict(features)[0]
        prediction_color = 'green' if prediction == 1 else 'red'
        prediction_message = 'Student is likely to pass' if prediction == 1 else 'Student is likely to fail'
        prediction_proba = model.predict_proba(features)[0, 1]  # Probability of the output being 1
        probability = np.round(prediction_proba * 100, 2)
        
        st.write(f'Final Prediction: :{prediction_color}[{prediction_message}]')
        st.write(f'Probability of student passing: :{prediction_color}[{probability}%]')
    
    st.markdown('<h6 style="text-align:center;">Powered by</h6>', unsafe_allow_html=True)
    try:
        with open(LOGO_STYLE_PATH) as f:
            st.markdown(f.read(), unsafe_allow_html=True)

        st.markdown(img_to_html(CMS_LOGO_PATH, 'svg', 'cms_logo'), unsafe_allow_html=True)

    except Exception as ex:
        print(f'Error displaying logo: {ex}')
        st.markdown('<h2 style="text-align:center; margin-top:5%; margin-bottom:-5%;">Catalyst Management Services</h2>', unsafe_allow_html=True)