#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for line in matrix:
        for num in line:
            print("{:d}".format(num), end=" " if num != line[-1] else "")
        print()
