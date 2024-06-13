# PROMPT:
"""
You are given a list of cities numbered from 1 to n and a list of roads connecting these cities. Each road connects two cities and has a certain cost associated with it. You need to find the minimum cost to connect all cities such that there is at least one path between any pair of cities.

Args:
- n (int): Number of cities.
- roads (List[Tuple[int, int, int]]): List of tuples representing roads. Each tuple contains three integers (u, v, cost) indicating a road between cities u and v with a cost of cost.

Returns:
- int: Minimum cost to connect all cities.

Example:
min_cost_to_connect_cities(5, [(1, 2, 1), (2, 3, 2), (3, 4, 3), (4, 5, 4), (5, 1, 5)]) => 10
"""
# SOLUTION:
def min_cost_to_connect_cities(n, roads):
    parent = [i for i in range(n + 1)]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        parent[find(x)] = find(y)
    
    roads.sort(key=lambda x: x[2])
    
    min_cost = 0
    for u, v, cost in roads:
        if find(u) != find(v):
            union(u, v)
            min_cost += cost
    
    return min_cost

# Example usage
print(min_cost_to_connect_cities(5, [(1, 2, 1), (2, 3, 2), (3, 4, 3), (4, 5, 4), (5, 1, 5)]))  # Output: 10
