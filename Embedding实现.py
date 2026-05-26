import torch
import torch.nn as nn
import math


class DeepSeekEmbedding(nn.Module):
    def __init__(self, vocab_size, d_model, max_seq_len=8192):
        super().__init__()
        self.token_embedding = nn.Embedding(vocab_size, d_model)
        self.d_model = d_model

        # 预计算RoPE位置编码
        self._precompute_rope(max_seq_len, d_model)

    def _precompute_rope(self, max_seq_len, d_model):
        """预计算旋转位置编码"""
        position = torch.arange(max_seq_len).unsqueeze(1)
        div_term = torch.exp(
            torch.arange(0, d_model, 2) *
            -(math.log(10000.0) / d_model)
        )

        # 计算sin和cos
        pe = torch.zeros(max_seq_len, d_model)
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)

        self.register_buffer('pe', pe.unsqueeze(0))

    def apply_rope(self, x, position_ids=None):
        """应用旋转位置编码"""
        if position_ids is None:
            position_ids = torch.arange(x.size(1), device=x.device)

        cos = self.pe[:, position_ids, 0::2].cos()
        sin = self.pe[:, position_ids, 1::2].sin()

        # 旋转操作
        x_rotated = torch.zeros_like(x)
        x_rotated[:, :, 0::2] = x[:, :, 0::2] * cos - x[:, :, 1::2] * sin
        x_rotated[:, :, 1::2] = x[:, :, 0::2] * sin + x[:, :, 1::2] * cos

        return x_rotated

    def forward(self, input_ids, position_ids=None):
        # 1. Token Embedding
        x = self.token_embedding(input_ids)

        # 2. 应用RoPE
        x = self.apply_rope(x, position_ids)

        return x * math.sqrt(self.d_model)  # 缩放因子