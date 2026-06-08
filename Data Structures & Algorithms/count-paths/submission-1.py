class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # We can optimize the space more by only considering 
        # the previous row
        grid = [1] * m
        
        # We use above and to the left
        # to calculate how many ways

        for row in range(1, n):
            new_row = [1] + [0] * (m - 1)
            for col in range(1, m):
                new_row[col] = grid[col] + new_row[col - 1]
            grid = new_row

        return grid[m - 1]