#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [[num ** 2 for num in line] for line in matrix]

    return new_matrix
