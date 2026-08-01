import torch


def multiply(A, B):
    if not A or not B or not A[0] or not B[0]:
        raise ValueError("matrices must not be empty")
    if any(len(row) != len(A[0]) for row in A):
        raise ValueError("A must be rectangular")
    if any(len(row) != len(B[0]) for row in B):
        raise ValueError("B must be rectangular")
    if len(A[0]) != len(B):
        raise ValueError("A columns must equal B rows")

    new_matrix = [[0 for col in range(len(B[0]))] for row in range(len(A))]
    for row in range(len(A)):
        for col in range(len(B[0])):
            val = 0
            for i in range(len(A[0])):
                val += A[row][i] * B[i][col]
            new_matrix[row][col] = val
    return new_matrix


def initial_matrix_multiplication(tokens, model):
    embedding = model.get_input_embeddings()
    if embedding is None or not hasattr(embedding, "weight"):
        raise ValueError("model does not expose an input embedding matrix")

    token_ids = torch.as_tensor(tokens, dtype=torch.long, device=embedding.weight.device)
    if token_ids.ndim != 1:
        raise ValueError("tokens must be a one-dimensional sequence of token IDs")
    if token_ids.numel() == 0:
        return embedding.weight.new_empty((0, embedding.weight.shape[1]))
    if torch.any(token_ids < 0) or torch.any(token_ids >= embedding.weight.shape[0]):
        raise ValueError("token ID is outside the model vocabulary")

    return torch.index_select(embedding.weight, 0, token_ids)
