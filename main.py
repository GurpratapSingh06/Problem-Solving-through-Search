"""Run and compare search algorithms for a weighted city graph."""
from search_algorithms.data import CITY_GRAPH, HEURISTIC
from search_algorithms.graph_search import (
    bfs, dfs, uniform_cost_search, greedy_best_first_search,
    a_star_search, hill_climbing,
)
from search_algorithms.n_queens import solve_n_queens, print_board


def display_result(result):
    print("\n" + "-" * 65)
    print(f"Algorithm       : {result.algorithm}")
    if result.success:
        print("Path            :", " -> ".join(result.path))
        print(f"Total path cost : {result.cost:g} km")
    else:
        print("Path            : No solution found")
        print("Total path cost : N/A")
    print("Nodes explored  :", result.nodes_explored)
    print(f"Execution time  : {result.execution_time:.8f} seconds")


def run_route_search():
    print("\nAVAILABLE CITIES:", ", ".join(CITY_GRAPH))
    start = input("Enter start city [Pune]: ").strip() or "Pune"
    goal = input("Enter goal city [Mumbai]: ").strip() or "Mumbai"

    if start not in CITY_GRAPH or goal not in CITY_GRAPH:
        print("Invalid city. Please choose from the available cities.")
        return

    algorithms = [
        bfs, dfs, uniform_cost_search,
        lambda g, s, d: greedy_best_first_search(g, HEURISTIC, s, d),
        lambda g, s, d: a_star_search(g, HEURISTIC, s, d),
        lambda g, s, d: hill_climbing(g, HEURISTIC, s, d),
    ]

    print(f"\nSEARCH ALGORITHM PERFORMANCE: {start} -> {goal}")
    for algorithm in algorithms:
        display_result(algorithm(CITY_GRAPH, start, goal))


def run_n_queens():
    try:
        n = int(input("Enter board size N: "))
        solved, board, nodes, elapsed = solve_n_queens(n)
        print("\nN-QUEENS RESULT")
        if solved:
            print(f"Solution for N = {n}: {board}")
            print_board(board)
        else:
            print(f"No solution exists for N = {n}.")
        print("Recursive calls :", nodes)
        print(f"Execution time  : {elapsed:.8f} seconds")
    except ValueError as error:
        print("Invalid input:", error)


def main():
    while True:
        print("\n" + "=" * 65)
        print("ARTIFICIAL INTELLIGENCE - PROBLEM SOLVING THROUGH SEARCH")
        print("=" * 65)
        print("1. Run city-route search algorithms")
        print("2. Solve N-Queens using Backtracking")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            run_route_search()
        elif choice == "2":
            run_n_queens()
        elif choice == "3":
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
