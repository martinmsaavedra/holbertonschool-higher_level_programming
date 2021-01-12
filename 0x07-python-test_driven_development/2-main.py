#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)
print("----")
print(matrix_divided(None, 3))
print("----")
print(matrix_divided(matrix, None))
print("----")
print(matrix_divided())