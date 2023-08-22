class Graph:
    def _init_(self):
        self.adj_list = {}
    
    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)
    
    def dfs(self, start, visited):
        visited.add(start)
        print(start, end=" ")
        
        if start in self.adj_list:
            for neighbor in self.adj_list[start]:
                if neighbor not in visited:
                    self.dfs(neighbor, visited)
                
if _name_ == "_main_":
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    
    print("DFS traversal:")
    visited = set()
    graph.dfs(0, visited)