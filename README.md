# DeepSequence-Recommender

![CI](https://img.shields.io/github/actions/workflow/status/Trojan3877/DeepSequence-Recommender/ci.yml)
![Python](https://img.shields.io/badge/python-3.10-blue)
![MLflow](https://img.shields.io/badge/MLflow-tracking-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-ready-success)
![Level](https://img.shields.io/badge/Engineering-L6%20ML%20System-purple)

## Overview

DeepSequence-Recommender is a production-ready sequence-based recommender system built using PyTorch.

---

## Architecture

```mermaid
flowchart LR
    DATA[User Interaction Data]
    PREP[Sequence Preprocessing]
    MODEL[LSTM Recommender Model]
    TRAIN[Training Loop]
    MFLOW[MLflow Tracking]
    API[FastAPI Inference API]
    CLIENT[Client App]

    DATA --> PREP --> MODEL
    MODEL --> TRAIN --> MFLOW
    TRAIN --> API --> CLIENT
DeepSequence-Recommender/
│
├── app/
│   ├── train.py
│   ├── evaluate.py
│   ├── infer_api.py
│   └── recommender.py
│
├── data/
│   ├── preprocessing.py
│   └── dataset.py
│
├── mlflow/
│   └── tracking.py
│
├── metrics.md
├── dailylog.md
├── contributing.md
├── tests/
│   ├── test_data.py
│   ├── test_recommender.py
│   └── test_api.py
├── requirements.txt
├── Dockerfile
├── .github/workflows/ci.yml
└── README.md  (LAST)

Quick Start
pip install -r requirements.txt
uvicorn app.infer_api:app --reload
