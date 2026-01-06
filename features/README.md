# Feature Store

## Purpose
Provide consistent features for both training and serving.

## Design
- Offline: Batch computed (Pandas / Spark)
- Online: Low-latency Redis access

## Guarantees
- Feature parity
- Versionable schemas
- No training/serving skew

## Why This Matters
Feature skew is the #1 silent failure in production ML systems.

## Ownership
Maintained by ML Platform team.