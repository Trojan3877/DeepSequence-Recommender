![Architecture](https://img.shields.io/badge/architecture-microservices-critical)
![Scalability](https://img.shields.io/badge/scalability-high-success)
![Latency](https://img.shields.io/badge/latency-<50ms-brightgreen)
![Observability](https://img.shields.io/badge/observability-enabled-blue)
![Security](https://img.shields.io/badge/security-scanned-success)
![CI](https://github.com/Trojan3877/DeepSequence-Recommender/actions/workflows/ci.yml/badge.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![Kubernetes](https://img.shields.io/badge/k8s-ready-informational)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

# DeepSequence Recommender

A production-grade **deep learning sequence recommendation** service.  
Built with the same enterprise architecture patterns as
[TrojanChat](https://github.com/Trojan3877/TrojanChat) — horizontally
scalable, observable, and secure.

## Architecture

```
Client (HTTP)
      ↓
FastAPI  →  BiLSTM + Attention model  →  top-k item recommendations
      ↓
  /metrics  →  Prometheus  →  Grafana
```

Full design details: [`docs/architecture.md`](docs/architecture.md)

## Quick Start

```bash
# 1. Clone and install
git clone https://github.com/Trojan3877/DeepSequence-Recommender.git
cd DeepSequence-Recommender
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 2. Configure
cp .env.example .env
# Edit .env with your SECRET_KEY

# 3. Run locally
uvicorn app.main:app --reload

# 4. Call the API
curl -X POST http://localhost:8000/recommendations/ \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u1", "item_sequence": ["item_1","item_2","item_3"], "top_k": 5}'
```

## Docker

```bash
docker-compose up --build
```

## Kubernetes

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/hpa.yaml
```

## Running Tests

```bash
pytest tests/ -v
```

## Metrics

`GET /metrics` — Prometheus scrape endpoint.  
See [`docs/metrics.md`](docs/metrics.md) for the full metrics catalogue.

## License

MIT
