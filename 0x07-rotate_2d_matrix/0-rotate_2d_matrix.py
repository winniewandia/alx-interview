#!/usr/bin/python3
"""a function that rotates a 2D matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """a function that rotates a 2D matrix 90 degrees clockwise

    Args:
        matrix (2D array): a 2D matrix
    """
    rotated_matrix = []
    for i in range(len(matrix[0])):
        new_row = []
        for j in range(len(matrix)):
            new_row.append(matrix[j][i])
        rotated_matrix.append(new_row[::-1])

    matrix[:] = rotated_matrix
