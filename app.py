import streamlit as st
import pandas as pd
import plotly.express as px

from resume_chatbot import answer_question
from resume_parser import extract_text_from_pdf
from ranking import rank_resumes
from skills_extractor import extract_skills
from ats_score import calculate_ats_score
from ai_feedback import generate_resume_feedback
from interview_generator import generate_questions

st.set_page_config(
    page_title="HireVision - Intelligent AI Recruitment Platform",
    page_icon="🤖",
    layout="wide"
)

# ---------- UI Styling ---------- #

st.markdown("""
<style>
.block-container{
padding-top:2rem;
}

[data-testid="stMetric"]{
background-color:#1e293b;
padding:20px;
border-radius:12px;
border:1px solid #334155;
}
</style>
""",unsafe_allow_html=True)

# ---------- Session Storage ---------- #

if "results" not in st.session_state:
    st.session_state.results = None

# ---------- Sidebar ---------- #
    
st.sidebar.title(" HireVision - AI Recruitment Platform")

page = st.sidebar.selectbox(
"Navigation",
[
"Dashboard",
"Resume Screening",
"Candidate Analysis",
"AI Feedback",
"Interview Questions",
"Analytics",
"Resume Chatbot"
]
)

# ---------- DASHBOARD ---------- #

if page == "Dashboard":

    st.title("AI Recruitment Dashboard")

    st.divider()

    col1,col2,col3 = st.columns(3)

    if st.session_state.results is not None:

        results = st.session_state.results

        total_resumes = len(results)
        top_score = results["Similarity Score"].max()
        avg_ats = round(results["ATS Score"].mean(),2)

    else:

        total_resumes = 0
        top_score = "--"
        avg_ats = "--"

    col1.metric("Total Resumes Processed", total_resumes)
    col2.metric("Top Candidate Score", top_score)
    col3.metric("Average ATS Score", avg_ats)

    st.divider()

    st.subheader("Platform Overview")

    st.write(
    """
    This AI platform automatically analyzes resumes,
    extracts candidate skills, calculates ATS scores,
    and helps recruiters shortlist candidates.
    """
    )

    if st.session_state.results is not None:

        st.subheader("Candidate Ranking Overview")

        fig = px.bar(
            st.session_state.results,
            x="Resume",
            y="Similarity Score",
            title="Candidate Ranking"
        )

        st.plotly_chart(fig,use_container_width=True)

# ---------- RESUME SCREENING ---------- #

elif page == "Resume Screening":

    st.title("Resume Screening System")

    col1,col2 = st.columns(2)

    with col1:
        job_description = st.text_area(
        "Enter Job Description",
        height=200
        )

    with col2:
        uploaded_files = st.file_uploader(
        "Upload Resumes",
        type=["pdf"],
        accept_multiple_files=True
        )

    if uploaded_files and job_description:

        resumes = []

        for file in uploaded_files:
            text = extract_text_from_pdf(file)
            resumes.append(text)

        scores = rank_resumes(job_description,resumes)

        job_skills = extract_skills(job_description)

        ats_scores = []

        for text in resumes:
            candidate_skills = extract_skills(text)
            ats = calculate_ats_score(job_skills,candidate_skills)
            ats_scores.append(ats)

        results = pd.DataFrame({

        "Resume":[file.name for file in uploaded_files],
        "Similarity Score":scores,
        "ATS Score":ats_scores

        }).sort_values(by="Similarity Score",ascending=False)

        st.session_state.results = results

        st.success(
        f"Top Candidate: {results.iloc[0]['Resume']} with score {results.iloc[0]['Similarity Score']}"
        )

        st.dataframe(results,use_container_width=True)

        fig = px.bar(
            results,
            x="Resume",
            y="Similarity Score",
            title="Candidate Ranking"
        )

        st.plotly_chart(fig,use_container_width=True)

# ---------- CANDIDATE ANALYSIS ---------- #

elif page == "Candidate Analysis":

    st.title("Candidate Skill Analysis")

    file = st.file_uploader("Upload Resume",type=["pdf"])

    if file:

        text = extract_text_from_pdf(file)

        skills = extract_skills(text)

        st.subheader("Detected Skills")

        st.write(skills)

# ---------- AI FEEDBACK ---------- #

elif page == "AI Feedback":

    st.title("AI Resume Feedback")

    file = st.file_uploader("Upload Resume",type=["pdf"])

    if file:

        text = extract_text_from_pdf(file)

        skills = extract_skills(text)

        feedback = generate_resume_feedback(skills)

        st.subheader("AI Suggestions")

        for f in feedback:
            st.write("•",f)

# ---------- INTERVIEW QUESTIONS ---------- #

elif page == "Interview Questions":

    st.title("Interview Question Generator")

    file = st.file_uploader("Upload Resume",type=["pdf"])

    if file:

        text = extract_text_from_pdf(file)

        skills = extract_skills(text)

        questions = generate_questions(skills)

        st.subheader("Recommended Interview Questions")

        for q in questions:
            st.write("•",q)

# ---------- ANALYTICS ---------- #

elif page == "Analytics":

    st.title("Hiring Analytics")

    uploaded_files = st.file_uploader(
    "Upload Resumes",
    type=["pdf"],
    accept_multiple_files=True
    )

    if uploaded_files:

        names = []
        lengths = []

        for file in uploaded_files:

            text = extract_text_from_pdf(file)

            names.append(file.name)
            lengths.append(len(text.split()))

        df = pd.DataFrame({

        "Candidate":names,
        "Resume Length":lengths

        })

        fig = px.bar(
        df,
        x="Candidate",
        y="Resume Length",
        title="Resume Content Size"
        )

        st.plotly_chart(fig,use_container_width=True)

        st.subheader("Skill Distribution Across Candidates")

        skills_count = {}

        for file in uploaded_files:

            text = extract_text_from_pdf(file)
            skills = extract_skills(text)

            for skill in skills:
                skills_count[skill] = skills_count.get(skill,0) + 1

        df_skills = pd.DataFrame({

        "Skill": list(skills_count.keys()),
        "Count": list(skills_count.values())

        })

        fig2 = px.bar(
        df_skills,
        x="Skill",
        y="Count",
        title="Top Skills in Candidates"
        )

        st.plotly_chart(fig2,use_container_width=True)

# ---------- RESUME CHATBOT ---------- #

elif page == "Resume Chatbot":

    st.title("AI Resume Chatbot")

    st.write(
    """
Upload a resume and ask questions about the candidate.

Example questions:
- What skills does this candidate have?
- What projects has the candidate worked on?
- Is this candidate suitable for a Python developer role?
"""
    )

    file = st.file_uploader("Upload Resume", type=["pdf"])

    if file:

        text = extract_text_from_pdf(file)

        st.success("Resume loaded successfully!")

        question = st.text_input("Ask a question about the candidate")

        if question:

            answer = answer_question(question,text)

            st.subheader("AI Answer")

            st.write(answer)

    else:

        st.info("Upload a resume to start asking questions.")