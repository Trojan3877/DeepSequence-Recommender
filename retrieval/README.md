# Candidate Retrieval Service (ANN)

## Purpose
Efficiently retrieve Top-K candidate items using vector similarity search
before expensive ranking models are applied.

## Technology
- FAISS (HNSW)
- FastAPI
- NumPy

## Performance
- Sub-linear search
- P95 latency < 20ms
- Recall@200 optimized

## Why Two-Stage?
Ranking all items is computationally infeasible at scale.
ANN reduces millions → hundreds.

## Next Stage
Candidates are passed to deep ranking models.

 How to Run Phase 1 Locally
Copy code
Bash
pip install faiss-cpu fastapi uvicorn numpy pandas scikit-learn
Copy code
Bash
python retrieval/build_item_embeddings.py
python retrieval/build_faiss_index.py
uvicorn retrieval.ann_service:app --reload