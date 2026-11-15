class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        """
        We could brute force and go through each node and have it be a root
        and then do BFS/DFS, but that would be O(n^2)
        Instead let's start at the leaves and then go to the root
        """
        if n == 1:
            return [0]

        adj_list = defaultdict(set)

        for start, end in edges:
            adj_list[start].add(end)
            adj_list[end].add(start)
        
        edge_count = {}
        leaves = deque()

        for src, neighbors in adj_list.items():
            if len(neighbors) == 1:
                leaves.append(src)
            edge_count[src] = len(neighbors)
        
        while leaves:
            # we start from the leaves and move in

            if n <= 2:
                # this means we have the root since 
                # either it is symmetrical or one single root
                return list(leaves)
            
            for _ in range(len(leaves)):
                # we do a BFS as we move up
                node = leaves.popleft()
                n -= 1
                for nei in adj_list[node]:
                    edge_count[nei] -= 1
                    if edge_count[nei] == 1:
                        leaves.append(nei)
        
