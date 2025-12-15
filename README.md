   AI Resume Screening & Skill Matching Tool

A professional AI-powered web application that analyzes resumes and matches them with job descriptions using NLP and Machine Learning techniques.

This project simulates a real-world Applicant Tracking System (ATS) used in the recruitment process.

    Features
- Upload resume in PDF format
- Extract and clean resume text
- Compare the resume with the job description
- Generate resume–job match percentage
- Identify matched skills
- Detect missing skills (skill gap analysis)
- Interactive and clean web UI using Streamlit

   Tech Stack
- Language: Python  
- NLP: Text Cleaning, TF-IDF  
- ML: Cosine Similarity  
- Frontend: Streamlit  
- PDF Parsing: PyPDF2  
- Version Control: Git, GitHub  


    System Workflow
1. User uploads a resume (PDF)
2. Resume text is extracted and cleaned
3. Job description text is processed
4. TF-IDF vectors are generated
5. Cosine similarity computes the match score
6. Skill overlap and gaps are identified
7. Results are displayed in the UI


   Use Cases
- Resume shortlisting
- Fresher screening
- HR automation
- ATS support systems
- Resume–JD compatibility analysis


  How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
