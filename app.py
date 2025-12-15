import streamlit as st
from PyPDF2 import PdfReader

from src.text_cleaner import clean_text
from src.matcher import calculate_match_score

st.set_page_config(page_title="AI Resume Screening", layout="centered")

st.title("AI Resume Screening & Skill Matching Tool")
st.write("Upload a resume and paste a job description to analyze compatibility.")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description here")

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for the reader page.pages:
        text += page.extract_text()
    return text

if resume_file and job_description:
    resume_text = extract_text_from_pdf(resume_file)

    clean_resume = clean_text(resume_text)
    clean_jd = clean_text(job_description)

    match_score = calculate_match_score(clean_resume, clean_jd)

    st.subheader(" Match Result")
    st.metric("Resume–Job Match Percentage", f"{match_score}%")
