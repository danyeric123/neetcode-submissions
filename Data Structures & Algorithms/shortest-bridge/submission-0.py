class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        # You need to first find an island and then 
        # move out from there with bfs until you 
        # hit the other island
        
        n = len(grid)
        dirs = (
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        )

        visited = set()

        def out_of_bounds(r,c):
            return (
                r < 0 or
                c < 0 or
                r == n or 
                c == n
            )

        def dfs(r,c):
            if out_of_bounds(r,c) or grid[r][c] == 0 or (r,c) in visited:
                return
            
            # You just need to visit it
            visited.add((r,c))

            for dx, dy in dirs:
                dfs(r+dx, c+dy)
        
        def bfs() -> int:
            dist = 0
            q = deque(visited)

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()

                    for dx, dy in dirs:
                        new_r, new_c = r+dx, c+dy
                        if out_of_bounds(new_r, new_c) or (new_r, new_c) in visited:
                            continue
                        if grid[new_r][new_c] == 1:
                            return dist
                        q.append((new_r, new_c))
                        visited.add((new_r, new_c))
                
                dist += 1
            
            return dist

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    # using DFS add to visited 
                    # so we have a starting point
                    # to branch out from
                    dfs(r,c)
                    return bfs()