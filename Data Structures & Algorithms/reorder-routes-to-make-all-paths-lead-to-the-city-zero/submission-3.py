import sys
sys.setrecursionlimit(10**6)
class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        # Start at city 0
        # recursively check its neighbors 

        # We can keep track of the direction the edges are going
        # by using negative and positve


        adj_list = defaultdict(list)

        for u, v in connections:
            adj_list[u].append(v)
            adj_list[v].append(-u)
        
        def dfs(node, parent):
            changes = 0

            for nei in adj_list[node]:
                if abs(nei) == parent:
                    # skip the reverse directions
                    continue
                
                # If going from nei to node would be positive
                # then this would need to be flipped and thus it
                # would be positive
                changes += dfs(abs(nei), node) + (nei > 0)
            
            return changes
        
        return dfs(0,-1)
                