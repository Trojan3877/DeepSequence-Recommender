from app.recommender import prepare_sequences

def test_sequence_prep():
    df = pd.DataFrame({"user":[0,0,0,0],"item":[1,2,3,4]})
    seqs = prepare_sequences(df, seq_len=3)
    assert len(seqs) == 1
