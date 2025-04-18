import streamlit as st
import PyPDF2 as pdf
#import docx
from google.generativeai import GenerativeModel
from IPython.display import Markdown
import google.generativeai as genai
from dotenv import load_dotenv
import os


# load the environment variables from the .env file
load_dotenv()

genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))

# -----------------------
# CONFIGURE YOUR GEMINI API
# -----------------------
  
model = GenerativeModel("gemini-1.5-flash-001")


# -----------------------
# TEXT EXTRACTORS
# -----------------------
def extract_text_from_pdf(file):
    reader = pdf.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.strip()


# -----------------------
# GENERATE FINAL RESPONSE
# -----------------------
def generate_cv_analysis(cv_text, job_description, model):
    prompt = f"""
You are a Job Application Optimization Assistant. You will receive:
1. The candidate's CV
2. The job description

Your tasks:
- Evaluate how well the candidate's CV matches the job description (score from 0 to 100).
- Highlight key strengths and gaps.
- Offer at least 3 personalized suggestions for improvement.
- Write a cover letter well suited for the job application. Keep it between 300 words.

Format your response as:

## JOB APPLICATION OPTIMIZER

### 1. CV MATCH SCORE: 85/100

### 2. STRENGHTS:
* Your detailed analysis here (WRITE IN FORM OF BULLET POINTS)

### 3. AREA OF IMPROVEMENT:
* A brief summary here (WRITE IN FORM OF BULLET POINTS)

 ### 4. RECOMMENDATIONS:
* Your suggestions here (WRITE IN FORM OF BULLET POINTS)

### 5. COVER LETTER
Write a professional cover letter of 300 words.

Candidate CV:
{cv_text}

Job Description:
{job_description}
"""
    response = model.generate_content(prompt)
    return response.text.strip()


#-----------------------
# STREAMLIT APP
# -----------------------
st.set_page_config(page_title="Job Application Optimizer", layout="wide")
st.title("🧠 Job Application Optimizer")
st.write("Upload your CV and paste a job description to get a tailored match score, improvement advice, and a professional cover letter!")

job_description = st.text_area("✍️ Paste Job Description Here", height=250)

uploaded_file = st.file_uploader("📄 Upload your CV (PDF)", type=["pdf"])

if uploaded_file and job_description:
    with st.spinner("🔍 Analyzing your CV..."):
        # Extract CV text
        if uploaded_file.name.endswith(".pdf"):
            cv_text = extract_text_from_pdf(uploaded_file)
        #elif uploaded_file.name.endswith(".docx"):
            #cv_text = extract_text_from_docx(uploaded_file)
        else:
            st.error("Unsupported file format. Please upload a PDF or DOCX.")
            st.stop()

        # Generate analysis
        final_output = generate_cv_analysis(cv_text, job_description, model)
        st.markdown(final_output)

