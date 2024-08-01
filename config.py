import joblib
import os

current_file_path = os.getcwd()
STUDENT_MODEL_ENGLISH = joblib.load(os.path.join(current_file_path, 'student_models', 'logistic_regression_model_eng.pkl'))
STUDENT_MODEL_MATH = joblib.load(os.path.join(current_file_path, 'student_models', 'logistic_regression_model_math.pkl'))
STUDENT_MODEL_SCIENCE = joblib.load(os.path.join(current_file_path, 'student_models', 'logistic_regression_model_sci.pkl'))
SCHOOL_MODEL_ENGLISH = joblib.load(os.path.join(current_file_path, 'school_models', 'school_model_eng_ka.pkl'))
SCHOOL_MODEL_MATH = joblib.load(os.path.join(current_file_path, 'school_models', 'school_model_eng_ka.pkl'))
SCHOOL_MODEL_SCIENCE = joblib.load(os.path.join(current_file_path, 'school_models', 'school_model_eng_ka.pkl'))

CMS_LOGO_PATH = os.path.join(current_file_path, 'static', 'images', 'cms_logo.svg')
LOGO_STYLE_PATH = os.path.join(current_file_path, 'static', 'html', 'logo_style.html')