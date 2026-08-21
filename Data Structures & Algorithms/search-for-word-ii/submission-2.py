class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        We will need to have Tries for words, 
        but backtrack when fail
        """

        word_break = "$"

        trie = {}

        for word in words:
            node = trie
            for let in word:
                if let not in node:
                    node[let] = {}
                node = node[let]
            
            node[word_break] = word
        
        rows, cols = len(board), len(board[0])
        visited = set()
        dirs = (
            (0,1),
            (1,0),
            (-1,0),
            (0,-1)
        )

        matched_words = []

        def backtrack(r: int, c: int, node: str) ->  None:
            
            # Check boundary and whether we have seen
            # it since do not want to wrap back and reuse letters
            if (
                r < 0 or
                c < 0 or
                r == rows or
                c == cols or
                board[r][c] not in node or
                (r,c) in visited
            ):
                return
            
            char = board[r][c]
            visited.add((r,c))
            parent_node = node
            node = node[char]

            if word_break in node:
                matched_words.append(node.pop(word_break))
            
            for dx, dy in dirs:
                backtrack(r+dx, c+dy, node)

            if not node:
                parent_node.pop(char)

            visited.remove((r,c))

        for row in range(rows):
            for col in range(cols):
                # Start from each of the cells
                if board[row][col] in trie:
                    backtrack(row, col, trie)
        
        return matched_words