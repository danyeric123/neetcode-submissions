class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i +1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                # if there is a violation of the sorting where
                # a substring is after the superstring
                return ""
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
            
        visited = {} # True means on path, while False just means visited, and none existence is not visited
        res = []

        def dfs(char: str) -> bool:
            if char in visited:
                return visited[char]
            
            visited[char] = True

            for neigh in adj[char]:
                if dfs(neigh):
                    return True
            
            visited[char] = False
            res.append(char)
        
        for char in adj:
            if dfs(char):
                return ""
        
        res.reverse()
        return "".join(res)