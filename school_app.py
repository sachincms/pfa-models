import streamlit as st
import joblib
import numpy as np

# Load the pre-trained logistic regression models
model_eng = joblib.load('school_model_eng_ka.pkl')
model_math = joblib.load('school_model_math_ka.pkl')
model_sci = joblib.load('school_model_sci_ka.pkl')

# Define the Streamlit app
def main():
    st.title('School Performance predictor using UDISE')
    
    # Dropdown to select subject
    subject = st.selectbox('Select Subject', ['English', 'Math', 'Science'])
    rural_urban_val = 0
    
    # Create sliders for input fields
    rural_urban = st.toggle('Rural/Urban (0 for Rural, 1 for Urban)')
    if rural_urban:
        rural_urban_val = 1
    school_vigilance = st.slider('School Vigilance', 0.0, 1.0, step=0.1)
    digi_index = st.slider('Digital Index', 0.0, 1.0, step=0.1)
    caste_diversity = st.slider('Caste Diversity', 0.0, 1.0, step=0.1)
    gender_ratio = st.slider('Gender Ratio', 0.0, 1.0, step=0.1)
    economic_diversity = st.slider('Economic Diversity', 0.0, 1.0, step=0.1)
    sanitation_index = st.slider('Sanitation Index', 0.0, 1.0, step=0.1)
    final_teacher_quality = st.slider('Final Teacher Quality', 0.0, 1.0, step=0.1)
    final_numbers_infra = st.slider('Final Numbers Infra', 0.0, 1.0, step=0.1)
    
    features = np.array([[rural_urban_val, school_vigilance, digi_index, caste_diversity, 
                          gender_ratio, economic_diversity, sanitation_index, 
                          final_teacher_quality, final_numbers_infra]])

    # Select the model based on the subject
    if subject == 'Math':
        model = model_math
    elif subject == 'Science':
        model = model_sci
    else:
        model = model_eng

    # When the user clicks the Predict button
    if st.button('Predict'):
        # Make a prediction
        prediction = model.predict(features)[0]
        prediction_proba = model.predict_proba(features)[0]
        
        # Get the class with the highest probability
        highest_proba_class = prediction_proba.argmax()
        highest_proba_score = prediction_proba[highest_proba_class]
        
        # Map the predicted class to its corresponding label
        class_labels = {
            0: 'Considerable improvement',
            1: 'High Improvement',
            2: 'Little Improvement',
            3: 'No Improvement'
        }
        predicted_label = class_labels.get(highest_proba_class, 'Unknown')

        # Display the prediction result
        st.write(f'Final Prediction: {predicted_label}')
        st.write(f'Probability of the predicted class: {highest_proba_score:.4f}')

if __name__ == '__main__':
    main()

