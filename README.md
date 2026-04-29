# 🚀 LLaMA4 from Scratch

A minimal, educational implementation of a **LLaMA-4 style Transformer with Mixture-of-Experts (MoE)** built completely from scratch in PyTorch.

This project is designed to help you understand how modern LLM architectures actually work — without relying on high-level libraries like HuggingFace Transformers.

---

## 📌 What This Project Covers

This repo walks through the full pipeline of building a small-scale LLM:

- Character-level tokenization
- Embedding layer initialization
- Transformer blocks:
  - Multi-Head Self Attention (MHA)
  - RMSNorm
  - Rotary Positional Embeddings (RoPE)
- Mixture-of-Experts (MoE) architecture:
  - Router (Top-K expert selection)
  - Expert MLPs
  - Shared expert pathway
- Training loop (causal language modeling)
- Text generation (autoregressive decoding)

---

## 🧠 Why This Exists

Most implementations of LLaMA-style models hide the core logic behind abstractions.

This repo focuses on:

- **Clarity over performance**
- **Understanding over scale**
- **Implementation over theory**

If you can build this, you actually understand LLMs — not just use them.

---

## ⚙️ Architecture Overview

This implementation follows a simplified version of modern LLaMA-4 style models:

- Transformer backbone
- RMSNorm instead of LayerNorm
- Rotary Positional Embeddings (RoPE)
- Mixture-of-Experts (MoE) instead of standard FFN

Each token is routed to a subset of experts using a learned router, improving parameter efficiency.

---

## 📂 Project Structure
'''LLaMA4_from_scratch/
│
├── model.py # Core transformer + MoE implementation
├── tokenizer.py # Character-level tokenizer
├── train.py # Training loop
├── generate.py # Text generation
├── config.py # Hyperparameters
└── notebook.ipynb # Step-by-step explanation (if applicable)'''

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Swetabhh/LLaMA4_from_scratch.git
cd LLaMA4_from_scratch
