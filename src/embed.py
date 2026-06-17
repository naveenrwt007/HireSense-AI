import json
import numpy as np
from tqdm import tqdm
from sentence_transformers import SentenceTransformer

INPUT_FILE = "outputs/candidate_profiles.json"

print("Loading profiles...")

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    profiles = json.load(f)

texts = [p["search_text"] for p in profiles]

print("Loading embedding model...")

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

print("Generating embeddings...")

embeddings = model.encode(
    texts,
    batch_size=64,
    show_progress_bar=True,
    normalize_embeddings=True
)

print("Shape:", embeddings.shape)

np.save(
    "models/candidate_embeddings.npy",
    embeddings
)

candidate_ids = [
    p["candidate_id"]
    for p in profiles
]

with open(
    "models/candidate_ids.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(candidate_ids, f)

print("Embeddings saved successfully")