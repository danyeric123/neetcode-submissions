class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # if we have more edges
        # then nodes than definitionally
        # there is a cycle
        if len(edges) > (n - 1):
            return False

        adj_list = defaultdict(list)

        for e1, e2 in edges:
            adj_list[e1].append(e2)
            adj_list[e2].append(e1)
        
        seen = set()

        def dfs(node: int, parent: int) -> bool:
            if node in seen:
                # Base case we saw this
                # and thus cycle
                return False
            
            seen.add(node)

            for nei in adj_list[node]:
                if nei == parent: continue

                if not dfs(nei, node):
                    return False
                
            return True

        
        # We need to not have cycles and also be
        # able to reach all nodes
        return dfs(0, -1) and len(seen) == n