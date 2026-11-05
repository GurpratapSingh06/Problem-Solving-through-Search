"""Default weighted city graph and heuristic values from the practical."""

CITY_GRAPH = {
    "Pune": {
        "Nashik": 120,
        "Ahmednagar": 100,
        "Satara": 200,
    },
    "Nashik": {
        "Mumbai": 200,
    },
    "Ahmednagar": {
        "Mumbai": 180,
    },
    "Satara": {
        "Mumbai": 100,
    },
    "Mumbai": {},
}

# Estimated remaining distance to Mumbai (heuristic h(n)).
HEURISTIC = {
    "Pune": 200,
    "Nashik": 140,
    "Ahmednagar": 90,
    "Satara": 80,
    "Mumbai": 0,
}
