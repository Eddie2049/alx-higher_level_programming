#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    _matrix = matrix.copy()
    len_ = len(matrix)
    for i in range(len_):
        _matrix[i] = [x**2 for x in matrix[i]]
    return (_matrix)
