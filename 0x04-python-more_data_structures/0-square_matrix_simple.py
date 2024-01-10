#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_ = []
    len_ = len(matrix)
    for i in matrix:
        matrix_.append([j*2 for j in i])
    return (matrix_)
