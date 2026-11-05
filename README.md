# AIML – Problem Solving Through Search

A Python implementation of search-based problem-solving techniques for the **TY B.Tech. Artificial Intelligence and Machine Learning Practical – Practical 2**.

The project demonstrates uninformed search, informed search, local search, and constraint satisfaction using a weighted city-route graph and the N-Queens problem.

## Algorithms implemented

| Category | Algorithm | Key idea |
|---|---|---|
| Uninformed | Breadth First Search (BFS) | Explores the graph level by level using a queue |
| Uninformed | Depth First Search (DFS) | Explores one branch deeply using a stack |
| Uninformed | Uniform Cost Search (UCS) | Expands the path with the lowest accumulated cost |
| Informed | Greedy Best-First Search | Selects the node with the smallest heuristic `h(n)` |
| Informed | A* Search | Uses `f(n) = g(n) + h(n)` |
| Local | Hill Climbing | Moves to a neighbour with a better heuristic value |
| CSP | N-Queens Backtracking | Places queens while checking row, column, and diagonal constraints |

## Project structure

```text
aiml-problem-solving-through-search/
│
├── main.py
├── README.md
├── search_algorithms/
│   ├── __init__.py
│   ├── data.py
│   ├── graph_search.py
│   └── n_queens.py
└── tests/
    └── test_search_algorithms.py
```

## Requirements

- Python 3.9 or later
- No third-party packages are required. The implementation uses Python's standard library.

## Setup and execution

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/aiml-problem-solving-through-search.git
cd aiml-problem-solving-through-search
```

### 2. Run the program

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

### 3. Select an option

```text
1. Run city-route search algorithms
2. Solve N-Queens using Backtracking
3. Exit
```

For route search, enter a start and goal city. Press Enter to use the defaults (`Pune` and `Mumbai`). For N-Queens, enter the board size `N`.

## Problem representation

### Weighted city graph

The practical uses the following directed weighted graph. Edge weights represent distances in kilometres.

```text
                 120
          +---- Nashik --------+
          |                    | 200
Pune -----+                    +---- Mumbai
          |                    | 180
          +-- Ahmednagar ------+
          |        100
          |
          +---- Satara --------+
                 200             100 to Mumbai
```

Exact edges:

| From | To | Distance |
|---|---|---:|
| Pune | Nashik | 120 km |
| Pune | Ahmednagar | 100 km |
| Pune | Satara | 200 km |
| Nashik | Mumbai | 200 km |
| Ahmednagar | Mumbai | 180 km |
| Satara | Mumbai | 100 km |

Heuristic values (estimated remaining distance to Mumbai):

| City | `h(n)` |
|---|---:|
| Pune | 200 |
| Nashik | 140 |
| Ahmednagar | 90 |
| Satara | 80 |
| Mumbai | 0 |

The graph and heuristic values are stored in `search_algorithms/data.py`. The graph is directed as defined by its adjacency dictionary.

## Performance measures

For each route-search algorithm, the program reports:

- **Path:** sequence of cities from source to destination.
- **Path cost:** sum of edge weights along the returned path.
- **Nodes explored:** number of nodes expanded/processed by that implementation.
- **Execution time:** elapsed wall-clock time measured using `time.perf_counter()`.

Execution time is machine- and run-dependent. Small graphs can produce very small timings, so compare algorithms over repeated runs or larger graphs for meaningful benchmarking.

## Important algorithm notes

- **BFS** minimises the number of edges, not necessarily total distance when edge weights differ.
- **DFS** does not guarantee a minimum-cost path.
- **UCS** finds a minimum-cost path for non-negative edge weights.
- **Greedy Best-First Search** prioritises `h(n)` and is not guaranteed to be optimal.
- **A\*** prioritises `g(n) + h(n)`. Its optimality depends on the heuristic and standard search assumptions.
- **Hill Climbing** uses only the current state and its neighbours. It may stop at a local optimum or plateau.
- **N-Queens** uses backtracking to ensure that no two queens share a column or diagonal. One queen is placed per row.

## Run tests

From the project root:

```bash
python -m unittest discover -s tests -v
```

The tests check that the algorithms find routes on the supplied graph, that UCS and A* return the minimum route cost for this example, and that the N-Queens solver handles solvable and unsolvable board sizes.

## Expected route-cost check

For the supplied graph, the possible Pune-to-Mumbai route costs are:

- Pune → Nashik → Mumbai = 120 + 200 = **320 km**
- Pune → Ahmednagar → Mumbai = 100 + 180 = **280 km**
- Pune → Satara → Mumbai = 200 + 100 = **300 km**

Therefore, the minimum route cost is **280 km**, through Ahmednagar. BFS may return a different route because it optimises edge count rather than weighted distance.

## Technologies used

- Python
- Python Standard Library
- `collections.deque` – BFS queue
- `heapq` – priority queues for UCS, Greedy, and A*
- `time.perf_counter()` – execution-time measurement
- Recursive functions – N-Queens backtracking
- `unittest` – basic automated tests

## Learning objectives

1. Understand state-space search and problem formulation.
2. Implement uninformed search algorithms.
3. Implement heuristic-based informed search algorithms.
4. Understand local search and its limitations.
5. Model and solve a constraint satisfaction problem.
6. Compare search algorithms using execution time, nodes explored, and path cost.

## Assignment scope

This repository is based on the supplied Practical 2 document, **Problem Solving Through Search**. It includes the city-route example, the stated heuristic values, the six graph-search methods, and N-Queens backtracking. UCS is implemented as well because it is included in the practical's theory and algorithm sections.



## License

This project is intended for academic learning and practical demonstration. You may add a license such as MIT if you want to permit reuse under its terms.
