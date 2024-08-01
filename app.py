import streamlit as st
import os
import sys
sys.path.append(os.getcwd())
from app_pages.StudentPerformance import student_performance
from app_pages.SchoolPerformance import school_performance

def main():
    
    pg = st.navigation(
        [
            st.Page(page=student_performance, title="Student Performance"),
            st.Page(page=school_performance, title="School Performance"),
        ]
    )

    pg.run()

if __name__ == '__main__':
    main()