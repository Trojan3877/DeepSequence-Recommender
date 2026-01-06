from retrieval.ann_service import retrieve_candidates
from reranking.reranker import rerank


def run_inference(user_embedding, ranked_items, blocked_items=None):
    """
    End-to-end inference orchestration.
    """
    # ranked_items assumed output of Phase 2
    final_items = rerank(ranked_items, blocked_items)
    return final_items