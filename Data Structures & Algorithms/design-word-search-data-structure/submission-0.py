class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        curr_trie = self.trie

        for char in word:
            if char not in curr_trie:
                curr_trie[char] = {}
            curr_trie = curr_trie[char]
        
        # Once we hit the end we need
        # to demark the ending
        curr_trie["!"] = {}

    def search(self, word: str) -> bool:
        return self._dfs(word, 0, self.trie)
    
    def _dfs(self, word: str, pos: int, trie: dict[str, dict]) -> bool:
        if len(word) == pos:
            # See if we hit a demarker
            return "!" in trie
        
        char = word[pos]

        if char == ".":
            for cand in trie:
                # go through the possible letters in
                # the level and see if we ever hit the
                # end of the word
                if self._dfs(word, pos + 1, trie[cand]):
                    return True
        
        if char in trie and self._dfs(word, pos + 1, trie[char]):
            # if we see that the char is in the level
            # and we finished the word at some point
            return True
        
        return False
        



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)