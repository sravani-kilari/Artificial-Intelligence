from collections import defaultdict

class Graph:
    def _init_(self):
        self.adj_list = defaultdict(list)
    
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
    
    def topological_sort(self):
        visited = set()
        stack = []
        
        def dfs(vertex):
            visited.add(vertex)
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    dfs(neighbor)
            stack.append(vertex)
        
        for vertex in self.adj_list:
            if vertex not in visited:
                dfs(vertex)
        
        return stack[::-1]

if _name_ == "_main_":
    graph = Graph()
    graph.add_edge(5, 2)
    graph.add_edge(5, 0)
    graph.add_edge(4, 0)
    graph.add_edge(4, 1)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)
    
    print("Topological Sort:")
    result = graph.topological_sort()
    print(result)