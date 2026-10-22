import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


# Find .env in the same folder as this Python file
BASE_DIR = Path(__file__).resolve().parent

ENV_FILE = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_FILE)


def generate_recommendations(
    resume_text,
    job_description,
    matching_skills,
    missing_skills
):

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:

        return (
            "OpenAI API key is not configured.\n\n"
            "Please check the .env file in the project folder."
        )

    client = OpenAI(
        api_key=api_key
    )

    matching = ", ".join(
        sorted(matching_skills)
    )

    missing = ", ".join(
        sorted(missing_skills)
    )

    prompt = f"""
You are an AI career assistant.

Analyze the candidate's resume against the job description.

Give simple and practical advice that a student can understand.

RESUME:
{resume_text[:12000]}

JOB DESCRIPTION:
{job_description[:12000]}

SKILLS ALREADY MATCHING:
{matching}

SKILLS MISSING FROM RESUME:
{missing}

Give your response in these sections:

### Overall Advice
Give 2 simple sentences about the resume-job match.

### Skills to Improve
Mention the 3 most important skills the candidate should improve.

### Resume Improvements
Give 3 practical suggestions for improving the resume for this job.

### What to Highlight
Mention the candidate's strongest relevant skills or projects.

Do not invent experience or skills that are not present in the resume.

Keep the response concise and easy to understand.
"""

    try:

        response = client.responses.create(
            model="gpt-6-luna",
            input=prompt
        )

        return response.output_text

    except Exception as e:

        return (
            "AI recommendation could not be generated.\n\n"
            f"Error: {str(e)}"
        )