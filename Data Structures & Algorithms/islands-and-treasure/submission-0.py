class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = (
            (0,1),
            (1,0),
            (-1,0),
            (0,-1)
        )

        q = deque([])
        visited = set()
        rows, cols = len(grid), len(grid[0])

        # Find all the treasure chests and go out from there

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))

        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                for dx, dy in dirs:
                    new_r, new_c = r + dx, c + dy
                    if (
                        new_r < 0 or 
                        new_c < 0 or
                        new_r == rows or
                        new_c == cols or
                        grid[new_r][new_c] == -1 or
                        (new_r, new_c) in visited
                    ): continue

                    visited.add((new_r, new_c))
                    q.append((new_r, new_c))

            dist += 1