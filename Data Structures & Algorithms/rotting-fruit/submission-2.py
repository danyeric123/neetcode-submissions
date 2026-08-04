class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        The key here is to start at the rotten and move out. It is
        similar to atlantic and pacific since it requires you to think
        the opposite of what you might expect.
        When you start at the rotten you do BFS from there.
        """

        fresh = 0

        dirs = (
            (0,1),
            (-1,0),
            (1,0),
            (0,-1)
        )
        q = deque([])

        row, col = len(grid), len(grid[0])

        time = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        # We want to go until the queue
        # is empty and we got all the fresh
        # And if the queue is empty but there
        # are still fresh then state is impossible
        while q and fresh > 0:

            for _ in range(len(q)):
                r, c = q.popleft()

                for dx, dy in dirs:
                    new_r, new_c = r+dx, c+dy
                    if (
                        new_r < 0 or
                        new_r == row or
                        new_c < 0 or
                        new_c == col or 
                        grid[new_r][new_c] != 1
                    ):
                        continue
                    grid[new_r][new_c] = 2
                    q.append((new_r, new_c))
                    fresh -= 1
            
            # once done with rot spreading then
            # increment time
            time += 1
        
        return time if fresh == 0 else -1