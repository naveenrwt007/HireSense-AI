import json
from tqdm import tqdm

lookup = {}

with open(
    "data/candidates.jsonl",
    "r",
    encoding="utf-8"
) as f:

    for line in tqdm(f):

        candidate = json.loads(line)

        lookup[
            candidate["candidate_id"]
        ] = candidate

with open(
    "models/candidate_lookup.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(lookup, f)

print("Lookup saved")