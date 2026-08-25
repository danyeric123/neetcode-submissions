class PrefixTree:

    def __init__(self):
        self._trie = {}

    def insert(self, word: str) -> None:
        curr = self._trie

        for let in word:
            if let not in curr:
                curr[let] = {}
            curr = curr[let]
        
        curr["!"] = {}


    def search(self, word: str) -> bool:
        curr = self._trie

        for let in word:
            if let not in curr:
                return False
            curr = curr[let]
        
        # Even if we exit the loop it could be 
        # that the word is part of one of the inserted words
        # But is not the end of any of the words
        return "!" in curr
        

    def startsWith(self, prefix: str) -> bool:
        curr = self._trie

        for let in prefix:
            if let not in curr:
                return False
            curr = curr[let]
        
        return True
        
        