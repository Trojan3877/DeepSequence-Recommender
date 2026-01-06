# Online Serving Layer

Purpose
Serve real-time recommendations with low latency
and high throughput.

Stack
- FastAPI (external API)
- gRPC (internal services)
- Redis (caching)

Performance Targets
- P95 latency < 50ms
- Cache hit rate > 80%

 Reliability
- Stateless services
- Horizontally scalable
- Cache-backed
How to Run Phase 5

Bash
pip install fastapi uvicorn redis grpcio
redis-server

Bash
uvicorn serving.api_gateway:app --reload