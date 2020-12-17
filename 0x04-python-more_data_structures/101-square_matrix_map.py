def square_matrix_map(matrix=[]):
    return list(map(lambda x: list(map(lambda y: y * y, x)), matrix))
