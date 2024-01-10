#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_ = matrix.copy()
    len_ = len(matrix_)
    for i in range(len_):
        matrix_[i] = list(map(lambda x: x**2, matrix[i]))
    return (matrix_)
