class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # can't have more edges than nodes (subtract 1 since
        # these are edges)
        if len(edges) > (n-1):
            return False

        # The point here is that we cannot have cycles

        seen = set()

        adj_list = defaultdict(list)

        for src, dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)
        
        def dfs(node: int, parent: int) -> bool:
            # we need a parent since we have bi-directional
            # edges and it is expected to "see" the parent
            # when visiting the child
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