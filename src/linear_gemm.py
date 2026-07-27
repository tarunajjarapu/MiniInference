def multiply(A, B):
    new_matrix = [[0 for col in range(len(B[0]))] for row in range(len(A))]
    for row in range(len(A)):
        for col in range(len(B[0])):
            val = 0
            for i in range(len(A[0])):
                val += A[row][i] * B[i][col]
            new_matrix[row][col] = val


first = [[1, 2, 3], [1, 2, 3]]
second = [[2], [2], [2]]
multiply(first, second)
