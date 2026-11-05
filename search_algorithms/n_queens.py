"""N-Queens CSP solved using recursive backtracking."""
from time import perf_counter


def solve_n_queens(n: int):
    """Return (solved, board, recursive_calls, execution_time).

    board[row] is the column containing the queen in that row.
    """
    if n < 1:
        raise ValueError("N must be at least 1.")

    board = [-1] * n
    recursive_calls = 0

    def is_safe(row: int, col: int) -> bool:
        for previous_row in range(row):
            previous_col = board[previous_row]
            if previous_col == col:
                return False
            if abs(previous_col - col) == abs(previous_row - row):
                return False
        return True

    def backtrack(row: int) -> bool:
        nonlocal recursive_calls
        recursive_calls += 1

        if row == n:
            return True

        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                if backtrack(row + 1):
                    return True
                board[row] = -1
        return False

    started = perf_counter()
    solved = backtrack(0)
    elapsed = perf_counter() - started
    return solved, board if solved else [], recursive_calls, elapsed


def print_board(board: list[int]) -> None:
    """Print a solved board using Q and . characters."""
    n = len(board)
    for row in range(n):
        print(" ".join("Q" if board[row] == col else "." for col in range(n)))
