# LLaMA4 From Scratch

A from-scratch implementation of Meta's Llama 4 architecture in pure Python
and PyTorch. Built to deeply understand how one of the most powerful
open-source LLMs works under the hood — not just how to use it.

## Overview

Llama 4 is Meta's latest open-source large language model, featuring a
Mixture-of-Experts (MoE) architecture with advanced attention mechanisms.
Instead of treating it as a black box, this project breaks down every
core component and rebuilds it from first principles.

## What's Implemented

- **Tokenizer** — text encoding and decoding pipeline, understanding
  how raw text gets converted into tokens the model can process
- **Attention Mechanism** — multi-head attention with the specific
  design choices Meta made in Llama 4, including rotary positional
  embeddings (RoPE)
- **Feedforward Layer** — the MLP block inside each transformer layer,
  including the SwiGLU activation function used in Llama 4

## Project Structure
## Project Structure
```
LLaMA4_from_scratch/
├── intro.md                  # Architecture overview & theory
├── tokenizer.py              # Tokenizer implementation
├── attention.py              # Attention mechanism
├── feedforward.py            # Feedforward layer
```
## Why This Project

Most people interact with LLMs through APIs without understanding
what's happening internally. I built this to go deeper — to understand
the architectural decisions behind Llama 4 and how modern LLMs are
actually structured at the code level.

This is part of my broader journey into deep learning research,
with a focus on LLM architecture and optimization.

## Stack

- Python 3.10+
- PyTorch

## Status

🚧 Work in progress — full model assembly and inference coming soon.
