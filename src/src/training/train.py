from model.transformer import TransformerRecommender

def train():
    print("Training Transformer Recommender...")
    model = TransformerRecommender(num_items=5000)
    print("Model initialized")

if __name__ == "__main__":
    train()
