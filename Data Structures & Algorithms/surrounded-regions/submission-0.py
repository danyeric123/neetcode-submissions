class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        You want to work in reverse by going from sides
        and then marking everything that counts as part of 
        unsurrounded region
        """
        dirs = (
            (0,1),
            (1,0),
            (-1,0),
            (0,-1)
        )
        rows, cols = len(board), len(board[0])

        def capture(r: int, c:int):
            if (
                r < 0 or 
                c < 0 or
                r == rows or
                c == cols or
                board[r][c] != "O"
            ):
                return
            
            board[r][c] = "T"

            for dx, dy in dirs:
                capture(r+dx, c+dy)
        
        for r in [0, rows -1]:
            for c in range(cols):
                if board[r][c] == "O":
                    capture(r,c)
        
        for c in [0, cols -1]:
            for r in range(rows):
                if board[r][c] == "O":
                    capture(r,c)
        
        for r in range(rows):
            for c in range(cols):
                # This was not marked as unsurrounded
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"
        