from search_engine import search_candidates

query = """
Machine Learning Engineer

Required Skills:
Python
PyTorch
NLP
LLM
Machine Learning

Experience:
5+ Years
"""

results = search_candidates(query)

print("\nTOP 5 EXPLAINABLE RESULTS\n")

for rank, r in enumerate(results[:5], start=1):

    print("=" * 60)

    print(f"Rank: {rank}")
    print(f"Name: {r['name']}")
    print(f"Role: {r['role']}")
    print(f"Experience: {r['experience']} Years")

    print(f"Final Score: {r['final_score']}")
    print(f"Semantic Score: {r['semantic_score']}")
    print(f"Skill Score: {r['skill_score']}")
    print(f"Experience Score: {r['experience_score']}")
    print(f"Signal Score: {r['signal_score']}")

    print(
        "Matched Skills:",
        ", ".join(r["matched_skills"])
        if r["matched_skills"]
        else "None"
    )

    print(
        "Missing Skills:",
        ", ".join(r["missing_skills"])
        if r["missing_skills"]
        else "None"
    )

    print("=" * 60)