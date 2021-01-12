#!/usr/bin/python3
"""TDD module"""


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")


def matrix_divided(matrix, div):
    """
    Divide matrix by div and return new matrix with new values
    """
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (array of arrays \
of integers/floats")

    largo = len(matrix[0])
    if largo == 0:
        raise TypeError("matrix must be a matrix (array of arrays \
of integers/floats")

    for elem in matrix:
        if largo != len(elem):
            raise TypeError("Each row of the matrix must have the same size")
        if type(elem) != list:
            raise TypeError("matrix must be a matrix (array of arrays \
of integers/floats")
        for val in elem:
                if type(val) != float and type(val) != int:
                    raise TypeError("matrix must be a matrix (array of arrays \
of integers/floats)")
    new_matrix = []
    for elem in range(len(matrix)):
        new_matrix.append([])
        for item in matrix[elem]:
            new_matrix[elem].append(round((item / div), 2))
    return new_matrix
