import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from huggingface_hub import hf_hub_download
from jd_parser import parse_jd

# -----------------------------
# SKILL NORMALIZATION
# -----------------------------

SKILL_MAP = {
    "llm": [
        "llm",
        "llms",
        "fine-tuning llms",
        "large language models",
        "transformers",
        "prompt engineering",
        "generative ai"
    ],

    "machine learning": [
        "machine learning",
        "ml"
    ],

    "nlp": [
        "nlp",
        "natural language processing"
    ],

    "pytorch": [
        "pytorch"
    ],

    "python": [
        "python"
    ]
}


def normalize_skill(skill):

    skill = skill.lower().strip()

    for canonical, aliases in SKILL_MAP.items():

        if skill in aliases:
            return canonical

    return skill


def skill_match_score(candidate_skills, required_skills):

    candidate_skills = {
        s.lower()
        for s in candidate_skills
    }

    required_skills = {
        s.lower()
        for s in required_skills
    }

    matched = candidate_skills & required_skills

    return len(matched) / max(
        len(required_skills),
        1
    )


def experience_score(candidate_exp, required_exp):

    if required_exp == 0:
        return 1.0

    if candidate_exp >= required_exp:
        return 1.0

    return candidate_exp / required_exp


def signal_score(signals):

    score = 0

    if signals.get("open_to_work_flag"):
        score += 0.3

    score += min(
        signals.get(
            "profile_completeness_score",
            0
        ) / 100,
        0.3
    )

    score += min(
        signals.get(
            "github_activity_score",
            0
        ) / 10,
        0.2
    )

    score += min(
        signals.get(
            "interview_completion_rate",
            0
        ),
        0.2
    )

    return score


def final_score(
    semantic,
    skill,
    experience,
    signal
):

    return (
        0.50 * semantic +
        0.25 * skill +
        0.15 * experience +
        0.10 * signal
    )


# -----------------------------
# LOAD ONCE
# -----------------------------

print("Loading model...")

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

print("Downloading artifacts from Hugging Face...")

index_path = hf_hub_download(
    repo_id="naveenrwt007/hiresense-models",
    filename="candidate_index.faiss"
)

ids_path = hf_hub_download(
    repo_id="naveenrwt007/hiresense-models",
    filename="candidate_ids.json"
)

lookup_path = hf_hub_download(
    repo_id="naveenrwt007/hiresense-models",
    filename="candidate_lookup.json"
)

print("Loading FAISS index...")

index = faiss.read_index(
    index_path
)

print("Loading candidate IDs...")

with open(
    ids_path,
    "r",
    encoding="utf-8"
) as f:

    candidate_ids = json.load(f)

print("Loading candidate lookup...")

with open(
    lookup_path,
    "r",
    encoding="utf-8"
) as f:

    lookup = json.load(f)

print("HireSense AI Ready ✓")


# -----------------------------
# MAIN FUNCTION
# -----------------------------

def search_candidates(jd_text):

    JD = parse_jd(jd_text)

    query_embedding = model.encode(
        [jd_text],
        normalize_embeddings=True
    ).astype("float32")

    scores, indices = index.search(
        query_embedding,
        100
    )

    results = []

    for semantic, idx in zip(
        scores[0],
        indices[0]
    ):

        cid = candidate_ids[idx]

        candidate = lookup[cid]

        profile = candidate["profile"]

        candidate_skills = [
            s["name"]
            for s in candidate["skills"]
        ]

        normalized_candidate_skills = [
            normalize_skill(s)
            for s in candidate_skills
        ]

        normalized_required_skills = [
            normalize_skill(s)
            for s in JD["required_skills"]
        ]

        skill_score_value = skill_match_score(
            normalized_candidate_skills,
            normalized_required_skills
        )

        exp_score_value = experience_score(
            profile["years_of_experience"],
            JD["required_experience"]
        )

        signal_score_value = signal_score(
            candidate["redrob_signals"]
        )

        final_score_value = final_score(
            float(semantic),
            skill_score_value,
            exp_score_value,
            signal_score_value
        )

        matched_skills = list(
            set(normalized_candidate_skills)
            &
            set(normalized_required_skills)
        )

        missing_skills = list(
            set(normalized_required_skills)
            -
            set(normalized_candidate_skills)
        )

        results.append({
            "candidate_id": cid,
            "name": profile["anonymized_name"],
            "role": profile["current_title"],
            "experience": profile["years_of_experience"],
            "semantic_score": round(float(semantic), 4),
            "skill_score": round(skill_score_value, 4),
            "experience_score": round(exp_score_value, 4),
            "signal_score": round(signal_score_value, 4),
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "final_score": round(final_score_value, 4)
        })

    results = sorted(
        results,
        key=lambda x: x["final_score"],
        reverse=True
    )

    return results[:10]