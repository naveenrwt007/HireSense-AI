# 🎯 AI Candidate Discovery & Ranking Engine

## Overview

Traditional recruitment systems rely heavily on keyword matching, causing recruiters to miss highly relevant candidates whose profiles may not contain exact keyword matches.

The **AI Candidate Discovery & Ranking Engine** solves this problem using **Semantic Search, Vector Embeddings, Hybrid Ranking, and Explainable AI** to identify and rank the most suitable candidates from a dataset of **100,000+ profiles**.

The system takes a **Job Description (JD)** as input and returns a ranked list of candidates along with transparent explanations for every ranking decision.

---

# 🚀 Features

## 🔎 Semantic Candidate Search

Uses **Sentence Transformers** to understand the meaning of a job description instead of relying on exact keyword matching.

## ⚡ FAISS Vector Retrieval

Performs fast similarity search across **100,000 candidate embeddings**.

## 🧠 Hybrid Ranking Engine

Ranks candidates using multiple signals:

- Semantic Similarity
- Skill Match Score
- Experience Match Score
- Recruiter Activity Signals

## 🔍 Explainable AI

Every recommendation includes:

- Final Score
- Semantic Score
- Skill Score
- Experience Score
- Signal Score
- Matched Skills
- Missing Skills

## 📊 Interactive Dashboard

Built with **Streamlit** for recruiter-friendly candidate discovery.

---

# 🏗️ System Architecture

```text
                    Job Description
                           │
                           ▼
                     JD Parser
                           │
                           ▼
              Sentence Transformer
                           │
                           ▼
                   Query Embedding
                           │
                           ▼
                    FAISS Search
                           │
                           ▼
              Hybrid Ranking Engine
                           │
                           ▼
                Explainable AI Results
                           │
                           ▼
                 Streamlit Dashboard
```

# 🛠️ Tech Stack

## Backend

- Python
- NumPy
- JSON

## AI / Machine Learning

- Sentence Transformers
- BAAI/bge-small-en-v1.5
- FAISS

## Frontend

- Streamlit


---

# 📂 Project Structure

```text
candidate-ranking-engine/

├── app/
│   └── app.py
├── data/
│   ├── candidate_schema.json
│   └── candidates.jsonl
├── models/
│   ├── candidate_embeddings.npy
│   ├── candidate_index.faiss
│   └── candidate_lookup.json
├── src/
│   ├── embed.py
│   ├── search_engine.py
│   ├── preprocess.py
│   └── jd_parser.py
├── README.md
└── requirements.txt
```

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/naveenrwt007/HireSense-AI.git
```

## Go Inside Project
```bash
cd HireSense-AI
```

## Create Environment
```
python -m venv venv
```

## Activate Environment
### Windows
```
venv\Scripts\activate
```
### Install Dependencies
```
pip install -r requirements.txt
```

# ▶️ Run Application
```
streamlit run app/app.py
```

## Python 3.13
```
streamlit run app/app.py --server.fileWatcherType none
```

# 📈 Ranking Formula
```
Final Score =

0.50 * Semantic Score +
0.25 * Skill Score +
0.15 * Experience Score +
0.10 * Signal Score
```

# 🔮 Future Enhancements
```
LLM-based JD Understanding
Resume Summarization
Candidate Clustering
Interview Fit Prediction
RAG-powered Recruiter Assistant
```

# 👨‍💻 Author
## Naveen Singh Rawat

AI Candidate Discovery & Ranking Engine


Now GitHub will render it correctly:
✅ Tech Stack as sections  
✅ Project tree with formatting  
✅ Commands with syntax highlighting  
✅ Future enhancements as bullets  
✅ Author section properly styled

Then:

```powershell
git add README.md
git commit -m "Fixed README markdown formatting"
git push origin main