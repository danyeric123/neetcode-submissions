class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # it will be whatever both atl and pac can reach
        # We reverse the cells to figure out which spots from
        # the oceans can we reach, not from a given cell to ocean

        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r: int, c: int, visited: set[tuple[int, int]], prev_height: int): 
            # Base case: Boundary, visited, not reachable
            if (
                r < 0 or
                c < 0 or
                r == rows or
                c == cols or
                (r,c) in visited or
                heights[r][c] < prev_height
            ):
                return
            
            visited.add((r,c))

            [
                dfs(r+dx, c+dy, visited, heights[r][c])
                for dx, dy in dirs
            ]
        

        for col in range(cols):
            dfs(0, col, pac, heights[0][col])
            dfs(rows-1, col, atl, heights[rows-1][col])

        for row in range(rows):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, cols - 1, atl, heights[row][cols-1])
        

        return list(pac & atl)