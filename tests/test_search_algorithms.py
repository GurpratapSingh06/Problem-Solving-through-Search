import unittest
from search_algorithms.data import CITY_GRAPH, HEURISTIC
from search_algorithms.graph_search import (
    bfs, dfs, uniform_cost_search, greedy_best_first_search,
    a_star_search, hill_climbing,
)
from search_algorithms.n_queens import solve_n_queens


class SearchAlgorithmTests(unittest.TestCase):
    def test_bfs_finds_route(self):
        result = bfs(CITY_GRAPH, "Pune", "Mumbai")
        self.assertTrue(result.success)
        self.assertEqual(result.path[0], "Pune")
        self.assertEqual(result.path[-1], "Mumbai")

    def test_dfs_finds_route(self):
        result = dfs(CITY_GRAPH, "Pune", "Mumbai")
        self.assertTrue(result.success)

    def test_ucs_minimum_cost(self):
        result = uniform_cost_search(CITY_GRAPH, "Pune", "Mumbai")
        self.assertTrue(result.success)
        self.assertEqual(result.cost, 280)

    def test_greedy_finds_route(self):
        result = greedy_best_first_search(CITY_GRAPH, HEURISTIC, "Pune", "Mumbai")
        self.assertTrue(result.success)

    def test_astar_finds_minimum_cost_route(self):
        result = a_star_search(CITY_GRAPH, HEURISTIC, "Pune", "Mumbai")
        self.assertTrue(result.success)
        self.assertEqual(result.cost, 280)

    def test_hill_climbing_finds_route_for_default_graph(self):
        result = hill_climbing(CITY_GRAPH, HEURISTIC, "Pune", "Mumbai")
        self.assertTrue(result.success)

    def test_four_queens(self):
        solved, board, calls, elapsed = solve_n_queens(4)
        self.assertTrue(solved)
        self.assertEqual(len(board), 4)
        self.assertGreater(calls, 0)

    def test_two_queens_has_no_solution(self):
        solved, board, calls, elapsed = solve_n_queens(2)
        self.assertFalse(solved)


if __name__ == "__main__":
    unittest.main()
