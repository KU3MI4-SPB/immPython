def transpose(matrix):
    transposed_matrix = [list(row) for row in zip(*matrix)]
    return transposed_matrix


matrix = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
transposed_matrix = transpose(matrix)
print(transposed_matrix)
