# LLaMA4 From Scratch

I built Llama 4's core architecture from scratch in pure Python and PyTorch —
not to use it, but to truly understand how it works at every level.

## Overview

Llama 4 is Meta's latest open-source large language model, built on a
Mixture-of-Experts (MoE) architecture with some genuinely interesting
design choices under the hood. Instead of just calling an API and moving
on, I wanted to know *why* it works — so I took it apart and rebuilt it
from first principles, component by component.

## What's Implemented

### Tokenizer — Byte Pair Encoding (BPE)
Built a BPE tokenizer completely from scratch. Starting from raw characters,
it iteratively merges the most frequent adjacent pairs to build a subword
vocabulary. Includes the full training loop with pair frequency counting,
greedy merging, and vocabulary tracking across 15 merge iterations.

### Attention Mechanism — Multi-Head + GQA + RoPE
Implemented the full `Llama4TextAttention` block, which includes:
- **Q, K, V projections** with separate head counts (16 query heads,
  4 key/value heads)
- **Grouped-Query Attention (GQA)** — K/V heads are shared across
  query groups via `repeat_kv`, reducing memory and compute
- **Rotary Positional Embeddings (RoPE)** — positions encoded via
  complex number rotations using `torch.view_as_complex` and
  element-wise multiplication in frequency space
- **QK Normalization** — optional L2 norm applied to Q and K after
  RoPE, before attention score computation
- **Scaled dot-product attention** with causal masking and softmax

### Feedforward Network — SwiGLU MLP
Implemented the `Llama4TextMLP` block with:
- **RMSNorm** pre-normalization (computed in float32 for stability,
  with a learnable gain parameter)
- **SwiGLU gating** — `down_proj(SiLU(gate_proj(x)) * up_proj(x))`
- Intermediate size calculated at `8/3 × hidden_size`, rounded up
  to the nearest multiple of 32
- **Residual connection** applied externally, matching Llama 4's
  actual decoder layer structure

## Project Structure
```
LLaMA4_from_scratch/
├── intro.md          # Architecture overview & theory
├── tokenizer.py      # BPE tokenizer from scratch
├── attention.py      # Multi-head attention with GQA + RoPE
└── feedforward.py    # SwiGLU MLP with RMSNorm
```

## Why I Built This

Most people use LLMs as black boxes — call the API, get the output, done.
I wanted to go deeper. This project is my attempt to understand the real
architectural decisions behind Llama 4, written in code I can actually
read, debug, and reason about.

Every design choice here — why GQA instead of full MHA, why RoPE over
learned embeddings, why SwiGLU over ReLU — has a reason. Building it
from scratch forced me to find those reasons.

This is part of my broader interest in deep learning research, specifically
how modern LLMs are designed and optimized at the architecture level.

## Stack

- Python 3.10+
- PyTorch

## Status

🚧 Work in progress — full decoder layer assembly and end-to-end
inference coming soon.
