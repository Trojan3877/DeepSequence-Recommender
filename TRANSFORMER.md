# Transformer-Based Recommender Model

## Overview
This project implements a sequence-aware Transformer recommender system designed to model temporal user-item interactions.

Unlike traditional collaborative filtering, this model captures:
- Order of interactions
- Long-range dependencies
- Contextual behavior shifts

## Architecture
- Embedding Layer (users, items)
- Positional Encoding
- Multi-Head Self-Attention
- Feed-Forward Network
- Output Projection

## Training Objective
- Loss Function: Cross-Entropy
- Optimizer: AdamW
- Regularization: Dropout + Weight Decay

## Evaluation Metrics
- Hit@10
- NDCG@10
- Mean Reciprocal Rank (MRR)

## Why Transformers?
Transformers outperform RNN/LSTM models on long user histories due to parallel attention and global context awareness.
