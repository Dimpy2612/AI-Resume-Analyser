
import streamlit as st

from resume_parser import extract_text_from_pdf

from analyzer import (
    extract_skills,
    compare_skills,
    calculate_similarity
)

from ai_recommendation import generate_recommendations


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("📄 AI Resume Analyzer & Job Matcher")

st.write(
    "Upload your resume and paste a job description "
    "to analyze your job compatibility."
)


# --------------------------------------------------
# Resume Upload
# --------------------------------------------------

resume_file = st.file_uploader(
    "📄 Upload Your Resume",
    type=["pdf"]
)


# --------------------------------------------------
# Job Description
# --------------------------------------------------

job_description = st.text_area(
    "💼 Paste Job Description",
    height=250,
    placeholder="Paste the complete job description here..."
)


# --------------------------------------------------
# Analyze Button
# --------------------------------------------------

if st.button(
    "🔍 Analyze Resume",
    type="primary"
):

    # --------------------------------------------------
    # Check Resume
    # --------------------------------------------------

    if resume_file is None:

        st.error(
            "Please upload your resume PDF."
        )

    # --------------------------------------------------
    # Check Job Description
    # --------------------------------------------------

    elif not job_description.strip():

        st.error(
            "Please paste a job description."
        )

    else:

        # --------------------------------------------------
        # Extract Resume Text
        # --------------------------------------------------

        with st.spinner("Reading your resume..."):

            resume_text = extract_text_from_pdf(
                resume_file
            )


        # --------------------------------------------------
        # Check Resume Text
        # --------------------------------------------------

        if not resume_text.strip():

            st.error(
                "Could not extract text from this PDF. "
                "Please upload a text-based PDF resume."
            )

        else:

            # --------------------------------------------------
            # Extract Skills
            # --------------------------------------------------

            resume_skills = extract_skills(
                resume_text
            )

            job_skills = extract_skills(
                job_description
            )


            # --------------------------------------------------
            # Skill Comparison
            # --------------------------------------------------

            (
                matching_skills,
                missing_skills,
                match_percentage
            ) = compare_skills(
                resume_skills,
                job_skills
            )


            # --------------------------------------------------
            # AI Semantic Similarity
            # --------------------------------------------------

            with st.spinner(
                "Calculating AI resume match..."
            ):

                semantic_score = float(
                    calculate_similarity(
                        resume_text,
                        job_description
                    )
                )


            # --------------------------------------------------
            # Resume Analysis
            # --------------------------------------------------

            st.divider()

            st.subheader(
                "📊 Resume Analysis"
            )


            # --------------------------------------------------
            # Metric Cards
            # --------------------------------------------------

            col1, col2, col3, col4 = st.columns(4)


            # AI Semantic Score
            with col1:

                st.metric(
                    "🤖 AI Semantic Score",
                    f"{semantic_score:.0f}%"
                )


            # Skill Match Score
            with col2:

                st.metric(
                    "🎯 Skill Match Score",
                    f"{float(match_percentage):.0f}%"
                )


            # Matching Skills
            with col3:

                st.metric(
                    "✅ Matching Skills",
                    len(matching_skills)
                )


            # Missing Skills
            with col4:

                st.metric(
                    "❌ Missing Skills",
                    len(missing_skills)
                )


            st.divider()


            # --------------------------------------------------
            # Matching Skills
            # --------------------------------------------------

            st.subheader(
                "✅ Matching Skills"
            )


            if matching_skills:

                for skill in sorted(
                    matching_skills
                ):

                    st.success(
                        f"✓ {skill.title()}"
                    )

            else:

                st.warning(
                    "No matching skills found."
                )


            # --------------------------------------------------
            # Missing Skills
            # --------------------------------------------------

            st.subheader(
                "❌ Missing Skills"
            )


            if missing_skills:

                for skill in sorted(
                    missing_skills
                ):

                    st.error(
                        f"✗ {skill.title()}"
                    )

            else:

                st.success(
                    "🎉 No major missing skills detected!"
                )


            # --------------------------------------------------
            # GENAI RECOMMENDATIONS
            # --------------------------------------------------

            st.divider()

            st.subheader(
                "🤖 AI Recommendations"
            )

            st.write(
                "Personalized suggestions generated from "
                "your resume and this job description."
            )


            with st.spinner(
                "Generating personalized AI recommendations..."
            ):

                ai_recommendations = generate_recommendations(
                    resume_text,
                    job_description,
                    matching_skills,
                    missing_skills
                )


            # --------------------------------------------------
            # Display AI Recommendations
            # --------------------------------------------------

            st.markdown(
                """
                <div style="
                    background-color:#f8fafc;
                    border:1px solid #e2e8f0;
                    border-radius:10px;
                    padding:20px;
                    margin-top:10px;
                ">
                """,
                unsafe_allow_html=True
            )


            st.markdown(
                ai_recommendations
            )


            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )


            # --------------------------------------------------
            # Simple Final Message
            # --------------------------------------------------

            st.divider()

            if semantic_score >= 75:

                st.success(
                    "🟢 Your resume has a strong overall match "
                    "with this job description."
                )

            elif semantic_score >= 55:

                st.warning(
                    "🟡 Your resume has a moderate match. "
                    "Check the AI recommendations above "
                    "to improve it."
                )

            else:

                st.info(
                    "🔴 Your resume needs improvement for "
                    "this particular job. Focus on the "
                    "missing skills and AI recommendations."
                )
