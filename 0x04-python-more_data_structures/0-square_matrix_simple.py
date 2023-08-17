#!/usr/bin/python3
# task 0

def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for w  in range(len(matrix)):
        new_matrix[w] = list(map(lambda x: x**2, matrix[w]))

    return (new_matrix)

