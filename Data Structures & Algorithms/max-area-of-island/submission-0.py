class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        dirs = (
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        )

        seen = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> int:
            if (
                r < 0 or 
                c < 0 or
                r == rows or 
                c == cols or
                grid[r][c] != 1 or
                (r,c) in seen
            ):
                return 0
            
            seen.add((r,c))
            curr_area = 1

            for dx, dy in dirs:
                curr_area += dfs(dx+r, dy+c)
            
            return curr_area
        
        for r in range(rows):
            for c in range(cols):
                if (
                    grid[r][c] == 1
                    and (r,c) not in seen
                ):
                    area = dfs(r,c)
                    max_area = max(max_area, area)
        
        return max_area