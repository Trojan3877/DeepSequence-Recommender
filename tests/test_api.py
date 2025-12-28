from fastapi.testclient import TestClient
from app.infer_api import app

def test_predict():
    client = TestClient(app)
    res = client.post("/predict", json=[1,2,3,4,5,6,7,8,9,10])
    assert res.status_code == 200
    assert "predictions" in res.json()
