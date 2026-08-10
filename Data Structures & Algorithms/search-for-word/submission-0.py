class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = (
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        )

        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r: int, c: int, word_pos:int) -> bool:
            # Base case we completed the word
            # needs to be before so we return true
            # even if "out of bounds" now
            if len(word) == word_pos:
                return True

            # Base case: out of bounds and already visited or not in word
            if (
                r < 0 or
                c < 0 or 
                r == rows or
                c == cols or
                board[r][c] != word[word_pos] or
                (r,c) in visited
            ):
                return False
            
            visited.add((r,c))

            for dx, dy in dirs:
                if dfs(r+dx, c+dy, word_pos+1):
                    return True
            
            # BACKTRACK: Remove current cell from visited set
            # This is crucial because when this path fails or completes,
            # we need to allow other paths to use this same cell.
            # Without this, once a cell is visited in any failed path,
            # it becomes permanently unavailable for other valid paths
            # that might start from different positions or directions.
            visited.remove((r,c))

            return False
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
            
        return False
