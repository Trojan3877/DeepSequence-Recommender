# Metrics

DeepSequence Recommender exposes a Prometheus scrape endpoint at `GET /metrics`.

## Exposed Metrics

| Metric | Type | Description |
|--------|------|-------------|
| `deepseq_active_requests` | Gauge | Currently in-flight recommendation requests |
| `deepseq_recommendations_total{status}` | Counter | Total recommendations served (labelled `success` or `error`) |
| `deepseq_recommendation_latency_seconds` | Histogram | End-to-end request latency |
| `deepseq_model_inference_latency_seconds` | Histogram | Neural model forward-pass latency |
| `deepseq_cache_hits_total` | Counter | Redis cache hits |
| `deepseq_cache_misses_total` | Counter | Redis cache misses |

## Prometheus Scrape Config

```yaml
scrape_configs:
  - job_name: 'deepsequence-recommender'
    static_configs:
      - targets: ['deepsequence-service:8000']
```

## SLO Targets

| SLO | Target |
|-----|--------|
| p50 recommendation latency | < 50 ms |
| p99 recommendation latency | < 250 ms |
| Model inference p50 latency | < 20 ms |
| Availability | ≥ 99.9 % |
| Error rate | < 0.1 % |
