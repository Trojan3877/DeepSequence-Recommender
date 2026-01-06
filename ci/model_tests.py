def test_ndcg_threshold(ndcg, threshold=0.4):
    assert ndcg >= threshold, "NDCG below production threshold"