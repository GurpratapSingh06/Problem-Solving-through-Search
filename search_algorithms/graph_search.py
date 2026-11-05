"""Graph search algorithms for the Pune-Mumbai route example.

All algorithms return a SearchResult containing the path, path cost,
number of expanded nodes, and execution time.
"""
from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter
from collections import deque
import heapq
from typing import Callable


@dataclass
class SearchResult:
    algorithm: str
    path: list[str] | None
    cost: float | None
    nodes_explored: int
    execution_time: float

    @property
    def success(self) -> bool:
        return self.path is not None


def _result(name, path, cost, nodes, started):
    return SearchResult(
        algorithm=name,
        path=path,
        cost=cost,
        nodes_explored=nodes,
        execution_time=perf_counter() - started,
    )


def bfs(graph: dict, start: str, goal: str) -> SearchResult:
    """Breadth First Search. Finds the fewest-edge path."""
    started = perf_counter()
    queue = deque([(start, [start], 0)])
    visited = set()
    nodes = 0

    while queue:
        current, path, cost = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        nodes += 1

        if current == goal:
            return _result("Breadth First Search (BFS)", path, cost, nodes, started)

        for neighbour, distance in graph.get(current, {}).items():
            if neighbour not in visited:
                queue.append((neighbour, path + [neighbour], cost + distance))

    return _result("Breadth First Search (BFS)", None, None, nodes, started)


def dfs(graph: dict, start: str, goal: str) -> SearchResult:
    """Depth First Search. The returned path is not necessarily optimal."""
    started = perf_counter()
    stack = [(start, [start], 0)]
    visited = set()
    nodes = 0

    while stack:
        current, path, cost = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        nodes += 1

        if current == goal:
            return _result("Depth First Search (DFS)", path, cost, nodes, started)

        # Reverse preserves the graph's displayed neighbour order in the traversal.
        for neighbour, distance in reversed(list(graph.get(current, {}).items())):
            if neighbour not in visited:
                stack.append((neighbour, path + [neighbour], cost + distance))

    return _result("Depth First Search (DFS)", None, None, nodes, started)


def uniform_cost_search(graph: dict, start: str, goal: str) -> SearchResult:
    """Uniform Cost Search. Expands the lowest accumulated-cost path."""
    started = perf_counter()
    frontier = [(0, start, [start])]
    best_cost = {start: 0}
    nodes = 0

    while frontier:
        cost, current, path = heapq.heappop(frontier)
        if cost != best_cost.get(current):
            continue
        nodes += 1

        if current == goal:
            return _result("Uniform Cost Search (UCS)", path, cost, nodes, started)

        for neighbour, distance in graph.get(current, {}).items():
            new_cost = cost + distance
            if new_cost < best_cost.get(neighbour, float("inf")):
                best_cost[neighbour] = new_cost
                heapq.heappush(frontier, (new_cost, neighbour, path + [neighbour]))

    return _result("Uniform Cost Search (UCS)", None, None, nodes, started)


def greedy_best_first_search(graph: dict, heuristic: dict,
                             start: str, goal: str) -> SearchResult:
    """Greedy Best-First Search. Prioritises the smallest h(n)."""
    started = perf_counter()
    frontier = [(heuristic.get(start, 0), start, [start], 0)]
    visited = set()
    nodes = 0

    while frontier:
        _, current, path, cost = heapq.heappop(frontier)
        if current in visited:
            continue
        visited.add(current)
        nodes += 1

        if current == goal:
            return _result("Greedy Best-First Search", path, cost, nodes, started)

        for neighbour, distance in graph.get(current, {}).items():
            if neighbour not in visited:
                heapq.heappush(
                    frontier,
                    (heuristic.get(neighbour, float("inf")),
                     neighbour, path + [neighbour], cost + distance)
                )

    return _result("Greedy Best-First Search", None, None, nodes, started)


def a_star_search(graph: dict, heuristic: dict,
                  start: str, goal: str) -> SearchResult:
    """A* Search using f(n) = g(n) + h(n)."""
    started = perf_counter()
    frontier = [(heuristic.get(start, 0), 0, start, [start])]
    best_cost = {start: 0}
    nodes = 0

    while frontier:
        _, cost, current, path = heapq.heappop(frontier)
        if cost != best_cost.get(current):
            continue
        nodes += 1

        if current == goal:
            return _result("A* Search", path, cost, nodes, started)

        for neighbour, distance in graph.get(current, {}).items():
            new_cost = cost + distance
            if new_cost < best_cost.get(neighbour, float("inf")):
                best_cost[neighbour] = new_cost
                priority = new_cost + heuristic.get(neighbour, 0)
                heapq.heappush(
                    frontier, (priority, new_cost, neighbour, path + [neighbour])
                )

    return _result("A* Search", None, None, nodes, started)


def hill_climbing(graph: dict, heuristic: dict,
                  start: str, goal: str) -> SearchResult:
    """Simple steepest-descent hill climbing using the goal heuristic.

    It moves to the unvisited neighbour with the smallest h(n), but only
    when that neighbour is strictly closer according to the heuristic.
    It can fail at local minima/plateaus and is not an optimal path algorithm.
    """
    started = perf_counter()
    current = start
    path = [current]
    cost = 0
    visited = {current}
    nodes = 1

    while current != goal:
        candidates = [
            (neighbour, distance)
            for neighbour, distance in graph.get(current, {}).items()
            if neighbour not in visited
        ]
        if not candidates:
            return _result("Hill Climbing", None, None, nodes, started)

        next_city, distance = min(
            candidates, key=lambda item: heuristic.get(item[0], float("inf"))
        )
        if heuristic.get(next_city, float("inf")) >= heuristic.get(
            current, float("inf")
        ):
            return _result("Hill Climbing", None, None, nodes, started)

        current = next_city
        visited.add(current)
        path.append(current)
        cost += distance
        nodes += 1

    return _result("Hill Climbing", path, cost, nodes, started)
