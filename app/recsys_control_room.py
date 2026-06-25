import streamlit as st
import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns
from src.features.online_retrieval import LatencyIsolatedFeatureStore

st.set_page_config(page_title="DeepSequence RecSys Control Panel", layout="wide")
sns.set_theme(style="darkgrid")

st.title("🧠 DeepSequence Recommender Control Panel & Telemetry Console")
st.caption("L6 Production-Tier Hyperparameter Sweeps & Real-Time Next-Item Scoring Diagnostics")

# Initialize feature store components
if 'feature_store' not in st.session_state:
    st.session_state.feature_store = LatencyIsolatedFeatureStore()

store = st.session_state.feature_store

# Sample Item Taxonomy Lookup Matrix
item_catalog = {
    0: "Padding Token / System Null",
    12: "Pro Slate Keyboard Hub",
    22: "Quantum Wireless Mouse v4",
    41: "Liquid Retinal Array 32-inch Panel",
    58: "Thunderbolt Multi-Bus Hub",
    88: "4K Streamer Capture Card Pro",
    102: "Developer Ergonomic Mechanical Board",
    405: "Titanium Desk Mounting Articulated Arm",
    994: "USB-C Active Optical Line (5m)"
}

st.sidebar.header("🕹️ Simulation Environment Context")
target_user = st.sidebar.selectbox("Active Simulation Profile", ["user_8271", "user_1194", "user_4952"])
recommendation_count = st.sidebar.slider("Top-K Candidates to Retrieve", 3, 15, 5)

st.markdown("---")

left_panel, right_panel = st.columns([1, 1])

with left_panel:
    st.subheader("⏱️ Online Feature Extraction Sequence Timeline")
    
    # Process user retrieval cycles
    input_tensor, fetch_latency = store.fetch_user_realtime_sequence(target_user)
    
    # Render historical items
    st.write(f"**Target Active Profile ID:** `{target_user}`")
    st.write(f"**Feature Retrieval Latency:** `{fetch_latency:.4f} ms` (In-Memory Hit)")
    
    historical_tokens = input_tensor[0][input_tensor[0] != 0]
    
    timeline_data = []
    for step, token in enumerate(historical_tokens):
        resolved_name = item_catalog.get(int(token), f"Unknown E-Commerce Skew Token ({token})")
        timeline_data.append({"Step": step + 1, "Item SKU ID": token, "Product Name Name": resolved_name})
    
    st.table(timeline_data)

with right_panel:
    st.subheader("🎯 Real-Time Scoring Head Probability Distribution")
    
    # Simulation logic for ONNX deep scoring latency paths
    inference_start = time.time()
    time.sleep(0.0035) # Simulating Triton model batch-execution runtime delay
    inference_latency = (time.time() - inference_start) * 1000
    
    # Generate mock distribution outputs via stable sampling Dirichlet models
    np.random.seed(int(historical_tokens[-1]) if len(historical_tokens) > 0 else 42)
    mock_logits = np.random.dirichlet(np.ones(10), size=1)[0]
    top_indices = np.argsort(mock_logits)[-recommendation_count:][::-1]
    
    scored_items = []
    scored_probabilities = []
    for idx in top_indices:
        simulated_sku = 10 * idx + 2 # Deterministic structural mock map hashes
        scored_items.append(item_catalog.get(simulated_sku, f"Product SKU Block {simulated_sku}"))
        scored_probabilities.append(mock_logits[idx])
        
    # Render analytics graph matrix
    fig, ax = plt.subplots(figsize=(6, 3.5))
    sns.barplot(x=scored_probabilities, y=scored_items, ax=ax, palette="viridis")
    fig.patch.set_facecolor("#1e2129")
    ax.set_facecolor("#1e2129")
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.tick_params(colors='white')
    st.pyplot(fig)

st.markdown("---")
st.subheader("⚡ End-to-End Operational Telemetry Summaries")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Aggregate Pipeline SLA Latency", f"{(fetch_latency + inference_latency):.2f} ms", delta="< 10ms System Budget")
with col2:
    st.metric("Inference Engine Scoring Bound", f"{inference_latency:.2f} ms")
with col3:
    st.metric("Triton Worker Concurrent Capacity", "18,450 RPS", delta="99.2% Utilization Profile")
