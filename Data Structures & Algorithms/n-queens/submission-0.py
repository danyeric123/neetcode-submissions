class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        solutions = []
        self.cols = set()
        self.pos_diag = set()
        self.neg_diag = set()
        self.backtrack(board, 0, solutions)
        return solutions

    def backtrack(self, board: list[list[str]], row: int, solutions: list[list[str]]) -> None:
        """
        We attempt to place the queen in a place and then backtrack
        to try all possibilities
        """
        if row == len(board):
            # Once on the final row, we know we finished
            solutions.append(["".join(row) for row in board])
            return
        for col in range(len(board)):
            if not self.is_valid(board, row, col):
                continue

            # Attempt position
            board[row][col] = "Q"
            self.cols.add(col)
            self.pos_diag.add(row + col)
            self.neg_diag.add(row - col)

            self.backtrack(board, row + 1, solutions)

            # Backtrack the decision
            board[row][col] = "."
            self.cols.remove(col)
            self.pos_diag.remove(row + col)
            self.neg_diag.remove(row - col)

    def is_valid(self, board, row, col):
        return (
            col not in self.cols
            and (row + col) not in self.pos_diag
            and (row - col) not in self.neg_diag
        )
