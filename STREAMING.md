# Real-Time Streaming Ingestion (Kafka)

## Purpose
Kafka enables near-real-time ingestion of user interaction events to support online inference and analytics.

## Event Flow
1. User interaction event emitted
2. Kafka producer publishes to topic
3. Consumer processes event
4. Event stored / forwarded to model

## Topics
- user_clicks
- impressions
- purchases

## Benefits
- Scalable ingestion
- Fault tolerance
- Replayability
- Decoupled architecture

## Design Considerations
- Partitioning by user_id
- At-least-once delivery
- Schema validation
