class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            row = [el for el in board[i] if el != "."]
            if len(row) != len(set(row)): return False

            col = [board[r][i] for r in range(9) if board[r][i] != "."]
            if len(col) != len(set(col)): return False
        
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                box = [board[r+dr][c+dc]
                   for dr in range(3) for dc in range(3)
                   if board[r+dr][c+dc] != "."]
                if len(set(box)) != len(box): return False
        
        return True