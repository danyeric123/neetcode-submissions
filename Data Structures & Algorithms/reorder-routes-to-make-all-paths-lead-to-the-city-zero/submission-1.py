import sys
sys.setrecursionlimit(10**6)

class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        # Start at city 0
        # recursively check its neighbors 

        # Set of edges representing directed roads (from a to b)
        self.edges = {(a, b) for a, b in connections}
        
        # Adjacency list for the undirected graph representation of cities
        self.neighbors = defaultdict(list)
        
        # Set to track visited cities
        self.visited = set()
        
        # Counter for the number of changes needed
        self.changes = 0

        # Build the adjacency list from the given connections
        for a, b in connections:
            self.neighbors[a].append(b)  # Add b as a neighbor of a
            self.neighbors[b].append(a)  # Add a as a neighbor of b (undirected representation)

        def dfs(city: int):
            self.visited.add(city)
            for nei in self.neighbors[city]:
                if nei in self.visited:
                    continue
                # Check if it is pointing in the right direction
                if (nei, city) not in self.edges:
                    self.changes += 1
                
                dfs(nei)
        
        dfs(0)
        return self.changes
