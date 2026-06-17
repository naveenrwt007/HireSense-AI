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