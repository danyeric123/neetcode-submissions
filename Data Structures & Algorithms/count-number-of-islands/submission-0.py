class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        rows, cols = len(grid), len(grid[0])

        dirs = (
            (0,1),
            (-1,0),
            (1,0),
            (0,-1)
        )
        visited = set()

        def dfs(r: int, c: int) -> None:
            # base case
            if (
                r < 0 or
                c < 0 or
                r == rows or
                c == cols or
                grid[r][c] == "0" or
                (r, c) in visited
            ):
                return
            
            visited.add((r,c))

            for dx, dy in dirs:
                dfs(r+dx, c+dy)
            
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    num_islands += 1
        
        return num_islands