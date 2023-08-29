def solve_graph(n, m, edges):
    # Create an adjacency list representation of the graph
    graph = [[] for _ in range(n + 1)]  # Using 1-based indexing
    
    # Populate the adjacency list
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Check if the graph is Eulerian
    is_eulerian = all(len(adj_list) % 2 == 0 for adj_list in graph[1:])
    
    if not is_eulerian:
        return -1
    
    # Initialize a list to store the directions of the edges
    directions = [0] * m
    
    # Perform a Depth-First Search (DFS) to assign directions
    def dfs(node):
        for neighbor in graph[node]:
            if directions[neighbor] == 0:
                directions[neighbor] = 1 - directions[node]
                dfs(neighbor)
    
    # Start DFS from any node (1 in this case)
    directions[1] = 0
    dfs(1)
    
    return directions

# Example Input
n, m = 4, 4
edges = [(1, 2), (1, 3), (2, 4), (3, 4)]

# Solve and print the result
result = solve_graph(n, m, edges)
if result == -1:
    print(-1)
else:
    print(" ".join(str(d) for d in result))
