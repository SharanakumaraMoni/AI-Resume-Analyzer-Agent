import streamlit as st
from crew_logic import run_crew
from tools import read_pdf

st.title("AI Resume Analyzer Agent 🤖")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if uploaded_file and job_desc:
        resume_text = read_pdf(uploaded_file)

        with st.spinner("Analyzing..."):
            result = run_crew(resume_text, job_desc)

        st.subheader("Result")
        st.write(result)
    else:
        st.warning("Please upload resume and enter job description")