import re

COMMON_SKILLS = [
    "python",
    "java",
    "c++",
    "sql",
    "aws",
    "gcp",
    "azure",
    "docker",
    "kubernetes",
    "pytorch",
    "tensorflow",
    "nlp",
    "llm",
    "machine learning",
    "deep learning",
    "airflow",
    "spark",
    "fastapi",
    "flask"
]


def parse_jd(jd_text):

    jd_lower = jd_text.lower()

    found_skills = []

    for skill in COMMON_SKILLS:
        if skill in jd_lower:
            found_skills.append(skill)

    exp_match = re.search(
        r'(\d+)\s*[-+]?\s*(\d+)?\s*years?',
        jd_lower
    )

    experience = 0

    if exp_match:
        experience = int(exp_match.group(1))

    return {
        "required_skills": found_skills,
        "required_experience": experience
    }

if __name__ == "__main__":

    jd = """
    Machine Learning Engineer

    Skills:
    Python
    PyTorch
    NLP
    LLM

    Experience: 5-9 years
    """

    print(parse_jd(jd))