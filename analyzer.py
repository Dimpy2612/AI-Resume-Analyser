from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


SKILLS = [
    "Python",
    "Java",
    "C++",
    "C",
    "SQL",
    "MySQL",
    "MongoDB",
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "Generative AI",
    "NLP",
    "Natural Language Processing",
    "TensorFlow",
    "PyTorch",
    "Scikit-learn",
    "Pandas",
    "NumPy",
    "AWS",
    "Azure",
    "Oracle Cloud",
    "Git",
    "GitHub",
    "Docker",
    "REST API",
    "Spring Boot",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "JSP",
    "Servlet",
    "Data Science",
    "Data Analysis",
    "R",
    "Tableau",
    "Power BI"
]


def extract_skills(text):
    text_lower = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills


def compare_skills(resume_skills, job_skills):

    resume_set = set(
        skill.lower() for skill in resume_skills
    )

    job_set = set(
        skill.lower() for skill in job_skills
    )

    matching_skills = resume_set.intersection(job_set)

    missing_skills = job_set - resume_set

    if len(job_set) > 0:
        match_percentage = (
            len(matching_skills) / len(job_set)
        ) * 100
    else:
        match_percentage = 0

    return (
        matching_skills,
        missing_skills,
        round(match_percentage, 2)
    )


# Load AI model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def calculate_similarity(resume_text, job_description):

    resume_embedding = model.encode(
        [resume_text]
    )

    job_embedding = model.encode(
        [job_description]
    )

    similarity = cosine_similarity(
        resume_embedding,
        job_embedding
    )[0][0]

    return round(
        similarity * 100,
        2
    )