# Architecture

## Overview

DeepSequence Recommender is a production-grade, horizontally scalable deep-learning sequence
recommendation service built on the same architectural principles as
[TrojanChat](https://github.com/Trojan3877/TrojanChat).

```
Client (HTTP / gRPC)
        ↓
Ingress / Load Balancer
        ↓
Kubernetes Cluster
        ↓
DeepSequence Pods (Replicas)
   ├── FastAPI layer  →  /recommendations
   ├── Model core     →  BiLSTM + Attention
   └── Metrics        →  /metrics  →  Prometheus → Grafana
        ↓
Redis (caching layer)
```

## Design Principles

### 1. Horizontal Scalability
- Stateless FastAPI workers – model weights are read-only at inference time.
- Redis for recommendation caching across replicas.
- Kubernetes HPA for CPU-based autoscaling.

### 2. Observability First
- `/metrics` exposes Prometheus gauges, counters, and histograms.
- Structured Python logging with configurable log-level.
- Health endpoint (`GET /recommendations/health`) for liveness probes.

### 3. Security by Design
- JWT token verification on protected endpoints.
- `SECRET_KEY` loaded from environment (never hard-coded).
- Bandit security scan enforced in CI.
- Non-root Docker runtime user.

### 4. ML Architecture
```
item_sequence  →  Embedding  →  BiLSTM  →  Attention  →  Linear  →  top-k items
```
- **Embedding layer** – maps item IDs to dense vectors (dim=64 by default).
- **BiLSTM encoder** – captures forward and backward temporal dependencies.
- **Scaled dot-product attention** – weights encoder outputs by relevance.
- **Linear projection** – maps the attended context to item logits.

### 5. CI/CD Pipeline
Every PR triggers:
1. `flake8` lint
2. `black` format check
3. `mypy` type checking
4. `bandit` security scan
5. `pytest` test suite

## Component Map

```
app/
 ├── main.py              – FastAPI app, startup, Prometheus mount
 ├── core/
 │    ├── config.py       – Pydantic settings
 │    ├── model.py        – DeepSequenceModel (BiLSTM + attention)
 │    ├── data_processor.py – SequenceProcessor (vocab, padding, encoding)
 │    ├── metrics.py      – Prometheus metrics
 │    └── security.py     – JWT helpers
 └── api/
      └── routes.py       – /recommendations endpoints

tests/
 └── test_recommender.py  – unit tests

k8s/
 ├── deployment.yaml
 ├── service.yaml
 └── hpa.yaml
```
