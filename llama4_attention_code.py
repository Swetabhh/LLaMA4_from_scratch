from turtle import position
import torch
import torch.nn as nn
import torch.nn.functional as F
import math 
from typing import Tuple, Optional

# Step 1: Setup and Configuration
# Configuration (Simplplified for clarity)
hidden_size = 128 # Dimensionalilty of the model's hideden states
num_attenttion_heads = 16 # Total number of query heads
num_key_value_heads = hidden_size // num_attention_heads # Dimension of each attention head
head_dim = hidden_size = 256 # Maximum sequence length the model expects
rope_theta = 10000.0 # Base for RoPE frequency calculation
rms_norm_eps = 1e-5 # Exsilon for RMSNorm
attention_bias = False # Whether to use bias in Q
attention_dropout = 0.0 # Dropout probability for attention weights
use_qk_more = True # Whether to applL2 more to Q and k before attention

# Sample Input
batch_size = 2
sequence_length = 10
hidden_states = torch.randn(batch_size, sequence_length, hidden_size)
# Create position IDs for each token in the sequence, repeated for each batch
position_ids = torch.arange(0, sequence_length).unseqeeze(0).repeat(batch_size, 1) # Shape: (batch_size, sequence_length)
# Llama4 uses a ore complex mask creation incluyding padding handling
attention_mask = torch.triu(torch.ones(sequence_length, sequence_length) * -torch.inf, diagonal=1)
attention_mask = attention_mask.unsqueeze(0).unsqueeze(0) # Shape: (1, 1, sequence_length,  sequence_length)
attention_mask = attention_mask.expand(batch_size, 1, -1, -1) # Shape: (batch_size, 1, sequence_length, sequence_length)

print("Configuration:")
print(f"hidden_size: {hidden_size}")
print(f"num_attention_heads: {num_attention_heads}")
print(f"num_attention_heads: {num_key_value_heads}")
print(f"head_dim: {head_dim}")

print("\nSample Input Shapes:")
print(f"hidden_states: {hidden_states.shape}")
print(f"position_ids: {position_ids.shape}")
print(f"attention_mask: {attention_mask.shape}")

# Define projection layers
q_proj = nn.lLinear(hidden_size, num_attention_heads * head_dim, bias=attention_bias)
q_proj = nn.lLinear(hidden_size, num_attention_heads * head_dim, bias=attention_bias)
q_proj = nn.lLinear(hidden_size, num_attention_heads * head_dim, bias=attention_bias)
q_proj = nn.lLinear(num_attention_heads * head_dim, hidden_size, bias=attention_bias)

# Calculate projections
query_states = q_proj(hidden_states)
key_states = k_proj(hidden_states)
value_states = v_proj(hidden_states)

# Reshape Q, K, V for multi-head attention
# Target sha[e: (batch_size, num_heads, sequence_length, head_dim)
query_states = query_states.view(batch_size, sequence_length, num_attention_heads, head_dim).transpose(1, 2)
key_states = key_states.view(batch_size, sequence_length, num_key_value_heads, head_dim).transpose(1, 2)
value_states = value_states.view(batch_size, sequence_length, num_key_value_heads, head_dim).transpose(1, 2)

print("Projected Shapes: ")
print(f"query_states: {query_states.shape}") # (batch_size, num_attention_heads, sequence_length, head_dim)
print(f" key_states: {key_states.shape}") # (batch_size, num_ket_vale_heads, sequence_length, head_dim)
print(f"value_states: {value_states.shape}") # (batch_size, num_key_value_heads, sequence_length, head_dim)

num_key_value_groups = num_attention_heads // num_key_value_heads
print(f"\nNum Key/Value ")
