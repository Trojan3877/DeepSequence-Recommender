from fastapi import FastAPI
from inference_pipeline_gpu import run_inference
import torch

app = FastAPI(title="DeepSequence GPU API")

@app.get("/health")
def health():
    return {
        "cuda_available": torch.cuda.is_available(),
        "device": str(torch.cuda.get_device_name(0)) if torch.cuda.is_available() else "CPU"
    }


@app.post("/recommend")
def recommend(sequence: list):
    results = run_inference(sequence)
    return {"recommendations": results}