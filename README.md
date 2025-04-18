# 💼 Job Application Optimizer with GenAI 🚀

An AI-powered resume optimization tool that helps job seekers tailor their CVs to job descriptions, providing targeted feedback and recommendations for improvement using Generative AI and Retrieval-Augmented Generation (RAG).


[👉 Try the App on Streamlit](https://job-application-optimizer-with-genai.streamlit.app/)

---

##  Features

-  **Job-CV Matching**: Analyze how well your resume aligns with a job description.

-  **LLM-Powered Feedback**: Get suggestions for improvement using Google's Gemini 1.5 Flash model.

-  **RAG System**: Retrieve high-quality, similar CVs from a curated vector store to improve recommendations.

-  **Structured Output**: Receive a detailed, JSON-like breakdown of your CV's match score, feedback, and missing elements.


---

## 🧱 Architecture

The solution integrates:

- **Gemini 1.5 Flash** for evaluation and feedback

- **ChromaDB** + **Gemini Embeddings** for resume similarity retrieval

- **Streamlit** for the interactive user interface


![image](https://github.com/user-attachments/assets/818e8d70-fa89-43ad-896c-4a71a2697c21)



---

## 🗂️ Project Structure

├── app.py # Main Streamlit app 

├── requirements.txt # Python dependencies 

├── .env # Environment variables 

├── .venv/ # Virtual environment 
---

## Getting Started

## 1. Clone the repository

git clone https://github.com/Timmtet/Job-Application-Optimizer-with-GenAI.git

cd Job-Application-Optimizer-with-GenAI


## 2. Set up your environment

python -m venv .venv

.venv\Scripts\activate on Windows

pip install -r requirements.txt


## 3. Add your Google API Key

Create a .env file (if running locally):

GOOGLE_API_KEY=your_google_api_key_here


## 4. Run the app

streamlit run app.py


## Acknowledgements

Google Gemini

ChromaDB

Streamlit

Kaggle



