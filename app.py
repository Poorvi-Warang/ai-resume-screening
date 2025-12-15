import streamlit as st
from PyPDF2 import PdfReader

st.set_page_config(page_title="AI Resume Screening", layout="centered")

st.title(" AI Resume Screening & Skill Matching Tool")
st.write("Upload a resume and paste a job description to analyze compatibility.")

# Upload resume
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# Job description input
job_description = st.text_area("Paste Job Description here")

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for the reader page.pages:
        text += page.extract_text()
    return text

if resume_file is None:
    resume_text = extract_text_from_pdf(resume_file)
    
    st.subheader(" Extracted Resume Text")
    st.text(resume_text[:3000]) 

if resume_file and job_description:
    st.success("Resume and Job Description received successfully!")
