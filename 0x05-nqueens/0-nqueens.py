#!/usr/bin/python3
"""solve the N queens problem
"""
import sys

"""this function checks if a queen can be
placed on a given row and column
without clashing with other queens"""


def clash_check(chessboard, row, col):
    # Check this row on the left side
    for i in range(col):
        if chessboard[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if chessboard[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i, j = row, col
    while i < len(chessboard) and j >= 0:
        if chessboard[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


"""This function solves the N queens problem using
backtracking and recursion
"""


def queen_place_soln(chessboard, col, solutions):
    if col == len(chessboard):
        solution = []
        for row in range(len(chessboard)):
            for col in range(len(chessboard)):
                if chessboard[row][col] == 1:
                    solution.append([row, col])
        solutions.append(solution)
        return True

    check = False
    for k in range(len(chessboard)):
        if clash_check(chessboard, k, col):
            chessboard[k][col] = 1
            check = queen_place_soln(chessboard, col + 1, solutions) or check
            chessboard[k][col] = 0  # BACKTRACK

    return check


"""this function returns all possible solutions
to the N queens problem for a given N"""


def n_queens(n):
    chessboard = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    queen_place_soln(chessboard, 0, solutions)
    return solutions


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = n_queens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
