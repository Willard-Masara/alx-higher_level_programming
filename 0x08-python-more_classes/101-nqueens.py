#!/usr/bin/python3
"""this is the advanced task on the chess problem"""

import sys

def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_util(board, 0, n)

def solve_util(board, row, n):
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_util(board, row + 1, n)
            board[row][col] = 0

def print_solution(board):
    n = len(board)
    solution = []
    for i in range(n):
        row = ''.join(['Q' if x == 1 else '.' for x in board[i]])
        solution.append(row)
    print('\n'.join(solution))
    print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
