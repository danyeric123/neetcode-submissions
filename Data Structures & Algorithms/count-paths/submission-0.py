class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(m)] for _ in range(n)]


        # For the top and right there is literally only one
        # way to get there--straight--since you cannot go left
        # or up
        for i in range(m): grid[0][i]=1
        for i in range(n): grid[i][0]=1
        
        # We use above and to the left
        # to calculate how many ways
        for row in range(1,n):
            for col in range(1,m):
                grid[row][col] = grid[row-1][col] + grid[row][col-1]
        
        return grid[n-1][m-1]