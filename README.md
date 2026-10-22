# AI Resume Analyzer & Job Matcher 🤖

An AI-powered web application that compares resumes with job descriptions, identifies matching and missing skills, calculates semantic similarity, and provides personalized AI recommendations to improve resumes and job compatibility.

## Features

- **Resume Upload:** Upload a resume in PDF format.
- **Skill Extraction:** Identify skills in the resume and job description.
- **Skill Matching:** Display matching skills and potential skill gaps.
- **Semantic Similarity:** Calculate a similarity score using Sentence Transformers.
- **GenAI Recommendations:** Generate personalized resume and career suggestions using the OpenAI API.
- **Simple Web Interface:** Use the application through a Streamlit interface.

## Tech Stack

- Python
- Streamlit
- NLP
- Sentence Transformers
- scikit-learn
- PyPDF
- OpenAI API
- python-dotenv

## Project Structure

```text
AI_Resume_Analyzer/
├── app.py
├── analyzer.py
├── resume_parser.py
├── ai_recommendation.py
├── requirements.txt
├── .env                 # Keep private; do not upload
└── venv/                # Local virtual environment; do not upload
```

## Setup and Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd AI-Resume-Analyzer-Job-Matcher
```

Replace `<YOUR_GITHUB_REPOSITORY_URL>` with your repository URL.

### 2. Create and activate a virtual environment

On macOS or Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If needed, make sure `requirements.txt` includes:

```text
streamlit
pypdf
sentence-transformers
scikit-learn
python-dotenv
openai
```

### 4. Configure the OpenAI API key

Create a `.env` file in the project root, alongside `app.py`, and add:

```text
OPENAI_API_KEY=your_new_openai_api_key
```

Replace the placeholder with your own valid API key. Never share your key or commit `.env` to GitHub. OpenAI API usage may incur separate charges.

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal, usually `http://localhost:8501`.

## How to Use

1. Upload your resume as a PDF.
2. Paste the job description into the text box.
3. Click **Analyze Resume**.
4. Review the semantic similarity score and skill match score.
5. Check matching skills and potential skill gaps.
6. Read the AI-generated recommendations, if the OpenAI API is configured.

## Security

Before pushing the project to GitHub, add the following to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.py[cod]
```

If an API key has been exposed, revoke it and create a new one.

## Future Improvements

- Improve skill extraction and normalize similar skill names.
- Support additional resume formats.
- Add resume improvement suggestions and downloadable reports.
- Expand testing with different resumes and job descriptions.

## Disclaimer

The match scores are estimates and should be used as guidance, not as a guarantee of hiring outcomes. Always verify that extracted skills and recommendations accurately reflect your experience.
