import torch

def export_model(model):
    scripted = torch.jit.script(model)
    scripted.save("model.pt")
