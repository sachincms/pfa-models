import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the pre-trained logistic regression models
model_eng = joblib.load('logistic_regression_model_eng.pkl')
model_math = joblib.load('logistic_regression_model_math.pkl')
model_sci = joblib.load('logistic_regression_model_sci.pkl')

# Define the Streamlit app
def main():
    st.title('Student Performance Predictor')
    
    # Dropdown to select subject
    subject = st.selectbox('Select Subject', ['English', 'Math', 'Science'])
    
    st.write("**Gender:** 0 for Female, 1 for Male")
    st.write("**Baseline Level (bl_level):** Integer values from 1 to 5")
    
    # Display input fields based on selected subject
    if subject == 'Math':
        # Create sliders for Math input fields
        Arithmetic_and_Number_Operations = st.slider('Arithmetic and Number Operations', 0.0, 1.0, step=0.05)
        Geometrical_Ideas = st.slider('Geometrical Ideas', 0.0, 1.0, step=0.05)
        Data_Handling_and_Statistics = st.slider('Data Handling and Statistics', 0.0, 1.0, step=0.05)
        Algebra_and_Mathematical_Reasoning = st.slider('Algebra and Mathematical Reasoning', 0.0, 1.0, step=0.05)
        Measurement = st.slider('Measurement', 0.0, 1.0, step=0.05)
        ProblemSolving_and_RealLife_Applications = st.slider('Problem Solving and Real Life Applications', 0.0, 1.0, step=0.05)
        Gender = st.selectbox('Gender', [0, 1])
        bl_level = st.slider('Baseline Level (bl_level)', 1, 5)

        features = np.array([[Arithmetic_and_Number_Operations, Geometrical_Ideas,
                              Data_Handling_and_Statistics, Algebra_and_Mathematical_Reasoning,
                              Measurement, ProblemSolving_and_RealLife_Applications, bl_level, Gender]])

        model = model_math
        
    elif subject == 'Science':
        # Create sliders for Science input fields
        Understanding_and_Analysis = st.slider('Understanding and Analysis', 0.0, 1.0, step=0.05)
        Identification_and_Classification = st.slider('Identification and Classification', 0.0, 1.0, step=0.05)
        Recall_and_Memory = st.slider('Recall and Memory', 0.0, 1.0, step=0.05)
        Understanding_Properties_and_Functions = st.slider('Understanding Properties and Functions', 0.0, 1.0, step=0.05)
        Measurement_and_Conversion = st.slider('Measurement and Conversion', 0.0, 1.0, step=0.05)
        Application_of_Concepts = st.slider('Application of Concepts', 0.0, 1.0, step=0.05)
        Gender = st.selectbox('Gender', [0, 1])
        bl_level = st.slider('Baseline Level (bl_level)', 1, 5)
        
        features = np.array([[Understanding_and_Analysis, Identification_and_Classification,
                              Recall_and_Memory, Understanding_Properties_and_Functions,
                              Measurement_and_Conversion, Application_of_Concepts, bl_level, Gender]])

        model = model_sci
        
    else:  # English
        # Create sliders for English input fields
        Language_Structure_and_Grammar = st.slider('Language Structure and Grammar', 0.0, 1.0, step=0.05)
        Vocabulary_and_Word_Usage = st.slider('Vocabulary and Word Usage', 0.0, 1.0, step=0.05)
        Reading_and_Comprehension = st.slider('Reading and Comprehension', 0.0, 1.0, step=0.05)
        Writing_and_Composition = st.slider('Writing and Composition', 0.0, 1.0, step=0.05)
        Contextual_and_Functional_Use_of_Language = st.slider('Contextual and Functional Use of Language', 0.0, 1.0, step=0.05)
        Gender = st.selectbox('Gender', [0, 1])
        bl_level = st.slider('Baseline Level (bl_level)', 1, 5)
        
        features = np.array([[Language_Structure_and_Grammar, Vocabulary_and_Word_Usage,
                              Reading_and_Comprehension, Writing_and_Composition,
                              Contextual_and_Functional_Use_of_Language, bl_level, Gender]])

        model = model_eng

    # When the user clicks the Predict button
    if st.button('Predict'):
        # Make a prediction
        prediction = model.predict(features)[0]
        prediction_proba = model.predict_proba(features)[0, 1]  # Probability of the output being 1
        
        # Display the prediction result
        st.write(f'Final Prediction: {prediction}')
        st.write(f'Probability of student Passing: {prediction_proba:.4f}')

if __name__ == '__main__':
    main()
