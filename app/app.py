import streamlit as st
import sys
import os
import json
import pandas as pd

# -----------------------------
# IMPORT SEARCH ENGINE
# -----------------------------

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "src"
        )
    )
)

from search_engine import search_candidates


# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="AI Candidate Discovery Engine",
    page_icon="🎯",
    layout="wide"
)

# -----------------------------
# HEADER
# -----------------------------

st.title("🎯 AI Candidate Discovery & Ranking Engine")

st.markdown("""
Find the best candidates using:

✅ Semantic Search  
✅ Skill Matching  
✅ Experience Matching  
✅ Recruiter Signals  
✅ Explainable AI Ranking
""")

# -----------------------------
# JD INPUT
# -----------------------------

jd = st.text_area(
    "Paste Job Description",
    height=300,
    placeholder="""
Machine Learning Engineer

Required Skills:
Python
PyTorch
NLP
LLM

Experience:
5+ Years
"""
)

# -----------------------------
# SEARCH BUTTON
# -----------------------------

if st.button("🚀 Search Candidates"):

    if not jd.strip():

        st.warning(
            "Please enter a Job Description."
        )

    else:

        with st.spinner(
            "Searching candidates..."
        ):

            results = search_candidates(jd)

        st.success(
            f"Found {len(results)} ranked candidates."
        )

        # -----------------------------
        # SUMMARY TABLE
        # -----------------------------

        table_data = []

        for rank, candidate in enumerate(
            results,
            start=1
        ):

            table_data.append({
                "Rank": rank,
                "Name": candidate["name"],
                "Role": candidate["role"],
                "Experience": candidate["experience"],
                "Final Score": candidate["final_score"]
            })

        st.subheader("🏆 Top Candidates")

        df = pd.DataFrame(table_data)

        st.dataframe(
            df,
            use_container_width=True
        )

        # -----------------------------
        # DETAILED VIEW
        # -----------------------------

        st.subheader(
            "🔍 Candidate Explanations"
        )

        for rank, candidate in enumerate(
            results,
            start=1
        ):

            with st.expander(
                f"#{rank} | {candidate['name']} | {candidate['role']}"
            ):

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "Final Score",
                        candidate["final_score"]
                    )

                    st.metric(
                        "Experience",
                        f"{candidate['experience']} Years"
                    )

                with col2:

                    st.metric(
                        "Semantic Score",
                        candidate["semantic_score"]
                    )

                    st.metric(
                        "Skill Score",
                        candidate["skill_score"]
                    )

                st.markdown("---")

                st.write(
                    f"**Experience Score:** {candidate['experience_score']}"
                )

                st.write(
                    f"**Signal Score:** {candidate['signal_score']}"
                )

                st.success(
                    "Matched Skills: " +
                    (
                        ", ".join(
                            candidate["matched_skills"]
                        )
                        if candidate["matched_skills"]
                        else "None"
                    )
                )

                st.warning(
                    "Missing Skills: " +
                    (
                        ", ".join(
                            candidate["missing_skills"]
                        )
                        if candidate["missing_skills"]
                        else "None"
                    )
                )

        # -----------------------------
        # DOWNLOAD RESULTS
        # -----------------------------

        st.subheader("📥 Export Results")

        st.download_button(
            label="Download Ranked Candidates JSON",
            data=json.dumps(
                results,
                indent=4
            ),
            file_name="ranked_candidates.json",
            mime="application/json"
        )