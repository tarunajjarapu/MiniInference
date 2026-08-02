import torch


@torch.inference_mode()
def initial_attention_step(hidden_states, model, layer_index=0):
    if hidden_states.ndim != 2:
        raise ValueError("hidden states must have shape (sequence length, hidden size)")

    layers = model.model.layers
    if layer_index < 0 or layer_index >= len(layers):
        raise ValueError("layer index is outside the model")

    layer = layers[layer_index]
    normalized_states = layer.input_layernorm(hidden_states)
    attention = layer.self_attn

    query_states = attention.q_proj(normalized_states)
    key_states = attention.k_proj(normalized_states)
    value_states = attention.v_proj(normalized_states)

    return query_states, key_states, value_states
