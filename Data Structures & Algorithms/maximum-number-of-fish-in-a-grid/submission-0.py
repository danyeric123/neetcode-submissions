class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        dirs = (
            (0, 1),
            (1,0),
            (-1,0),
            (0,-1)
        )

        seen = set()
        rows, cols = len(grid), len(grid[0])
        max_fish = 0

        def dfs(r:int,c:int) -> int:
            if (
                r <0 or
                c < 0 or 
                r == rows or 
                c == cols or
                (r, c) in seen
                or grid[r][c] == 0
            ):
                return 0
            
            fish = grid[r][c]
            seen.add((r,c))

            for dx, dy in dirs:
                fish += dfs(dx+r, dy+c)
            
            return fish
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0 and (r,c) not in seen:
                    fish = dfs(r,c)
                    max_fish = max(fish, max_fish)
        
        return max_fish