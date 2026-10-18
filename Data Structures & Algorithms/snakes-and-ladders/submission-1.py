from collections import deque

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        """
        Since this is "minimum number" then we can just do BFS
        since the fastest route will come first
        """

        len_board = len(board)

        # Calculate the position
        # reversing makes it easier
        board.reverse()
        def int_to_pos(square: int) -> tuple[int,int]:
            r = (square - 1) // len_board
            c = (square - 1) % len_board 
            
            if r % 2: 
                c = len_board - 1 - c
            
            return (r,c)
        
        q = deque([(1,0)]) # square, moves
        visited = set()

        while q:
            square, moves = q.popleft()

            for i in range(1,7):
                next_square = square + i
                r, c = int_to_pos(next_square)

                # We need to be able to check square
                # since we could jump somewhere in this move
                if board[r][c] != -1:
                    next_square = board[r][c]
                
                if next_square == len_board ** 2:
                    return moves + 1
                
                if next_square in visited: continue

                visited.add(next_square)
                q.append((next_square, moves + 1))
        
        return -1
