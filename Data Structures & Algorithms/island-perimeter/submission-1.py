class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        dirs = (
            (1,0),
            (0,1),
            (-1, 0),
            (0,-1)
        )

        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> int:
            if (
                r < 0 or
                c < 0 or
                r == rows or 
                c == cols or
                grid[r][c] == 0
            ):
                # if we it the outside
                # of island then that is 1
                return 1
            
            if (r, c) in visited:
                return 0
            
            perimeter = 0
            visited.add((r,c))

            for dx, dy in dirs:
                # every time i end up out of bounds
                # or hit water I am hitting a perimeter
                # so add
                perimeter += dfs(r+dx, c+dy)
            
            return perimeter
            

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # if we hit land then
                    # calculate perimeter
                    return dfs(r, c)