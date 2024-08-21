import joblib
import os

current_file_path = os.getcwd()
STUDENT_MODEL_ENGLISH_ODISHA = joblib.load(os.path.join(current_file_path, 'student_models', 'od_eng_logit.pkl'))
STUDENT_MODEL_MATH_ODISHA = joblib.load(os.path.join(current_file_path, 'student_models', 'od_math_logit.pkl'))
STUDENT_MODEL_SCIENCE_ODISHA = joblib.load(os.path.join(current_file_path, 'student_models', 'od_sci_logit.pkl'))
STUDENT_MODEL_ENGLISH_KARNATAKA = joblib.load(os.path.join(current_file_path, 'student_models', 'ka_eng_logit.pkl'))
STUDENT_MODEL_MATH_KARNATAKA = joblib.load(os.path.join(current_file_path, 'student_models', 'ka_math_logit.pkl'))
STUDENT_MODEL_SCIENCE_KARNATAKA = joblib.load(os.path.join(current_file_path, 'student_models', 'ka_sci_logit.pkl'))
SCHOOL_MODEL_ENGLISH = joblib.load(os.path.join(current_file_path, 'school_models', 'school_model_eng_ka.pkl'))
SCHOOL_MODEL_MATH = joblib.load(os.path.join(current_file_path, 'school_models', 'school_model_eng_ka.pkl'))
SCHOOL_MODEL_SCIENCE = joblib.load(os.path.join(current_file_path, 'school_models', 'school_model_eng_ka.pkl'))

CMS_LOGO_PATH = os.path.join(current_file_path, 'static', 'images', 'cms_logo.svg')
PFA_LOGO_PATH = os.path.join(current_file_path, 'static', 'images', 'transform.png')
LOGO_STYLE_PATH = os.path.join(current_file_path, 'static', 'html', 'logo_style.html')
PFA_LOGO_STYLE_PATH = os.path.join(current_file_path, 'static', 'html', 'pfa_logo_style.html')
DOCUMENTATION_PATH = os.path.join(current_file_path, 'static', 'html', 'documentation.html')