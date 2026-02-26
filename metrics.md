A/B Experiment Results
Model
Recall@10
NDCG@10
A (Baseline GRU)
0.389
0.241
B (Transformer)
0.421
0.287
Prometheus Telemetry Snapshot
Metric
Value
Avg API Latency
28 ms
p95 Latency
57 ms
Throughput
240 req/sec
Error Rate
0%
 Load Test Summary
Test Duration: 5 minutes
Concurrent Users: 100
Peak Throughput: 240 RPS
Zero timeouts
Stable memory usage

Snowflake Logging
All evaluation runs are automatically persisted to Snowflake with model version tagging, enabling experiment traceability and reproducibility.
A/B Routing
Traffic is deterministically split by user_id seed to ensure stable cohorting across sessions.
Observability
Prometheus exposes:
api_requests_total
api_latency_seconds
active_requests
Load Testing Summary
Users
Peak RPS
Avg Latency
p95
Errors
100
240
28 ms
57 ms
0%