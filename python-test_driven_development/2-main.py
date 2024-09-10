#!/usr/bin/python3

matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [[1, 2, 3], [4, 5]]
print(matrix)
print(matrix_divided(matrix, 3))
print()
print('-'*15)
print()
matrix = [[1, 2], [4, 5, 6]]
print(matrix)
print(matrix_divided(matrix, 3))
print()
print('-'*15)
print()
matrix = [[1, 2, 3], [4, 5, 6, 7]]
print(matrix)
print(matrix_divided(matrix, 3))
print()
print('-'*15)
print()
matrix = [[1, 2, 3, 7], [4, 5, 6]]
print(matrix)
print(matrix_divided(matrix, 3))
print()
print('-'*15)
print()
matrix = [[1, 2, 3, 7],[]]
print(matrix)
print(matrix_divided(matrix, 3))
print()
print('-'*15)
print()
matrix = [[], [4, 5, 6]]
print(matrix)
print(matrix_divided(matrix, 3))
print()
print('-'*15)
print()
matrix = [[1, 2, 3, 7], [None]]
print(matrix)
print(matrix_divided(matrix, 3))
print()
print('-'*15)
print()
matrix = [[None], [4, 5, 6]]
print(matrix)
print(matrix_divided(matrix, 3))
print()
print('-'*15)
print()
matrix = [[1, 2, 3, 7], [4, 5, 6], [7, 8, 9]]
print(matrix)
print(matrix_divided(matrix, 3))
print()
print('-'*15)
print()
