import json

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    first = json.loads(next(f))

print(first)