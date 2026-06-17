import json
from tqdm import tqdm

INPUT_FILE = "data/candidates.jsonl"
OUTPUT_FILE = "outputs/candidate_profiles.json"


def build_candidate_text(candidate):

    profile = candidate.get("profile", {})

    headline = profile.get("headline", "")
    summary = profile.get("summary", "")
    experience = profile.get("years_of_experience", 0)

    skills = [
        skill["name"]
        for skill in candidate.get("skills", [])
    ]

    career_text = ""

    for job in candidate.get("career_history", []):
        career_text += f"""
        Company: {job.get('company','')}
        Role: {job.get('title','')}
        Description: {job.get('description','')}
        """

    education_text = ""

    for edu in candidate.get("education", []):
        education_text += f"""
        Degree: {edu.get('degree','')}
        Field: {edu.get('field_of_study','')}
        """

    searchable_text = f"""
    Headline: {headline}

    Summary:
    {summary}

    Experience:
    {experience} years

    Skills:
    {", ".join(skills)}

    Career:
    {career_text}

    Education:
    {education_text}
    """

    return searchable_text


profiles = []

with open(INPUT_FILE, "r", encoding="utf-8") as f:

    for line in tqdm(f):

        candidate = json.loads(line)

        profiles.append({
            "candidate_id": candidate["candidate_id"],
            "search_text": build_candidate_text(candidate)
        })

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(profiles, f)

print("Profiles created:", len(profiles))