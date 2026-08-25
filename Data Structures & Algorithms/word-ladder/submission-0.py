class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # Create an adj list
        # for what words can go to
        # what other word
        adj_list = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for pos in range(len(word)):
                pattern = word[:pos] + "*" + word[pos+1:]
                adj_list[pattern].append(word)
        
        # We then do a BFS to see if we 
        # can get to the word and do Djikstra's
        q = deque([beginWord])
        seen = set([beginWord])
        
        # You need it to be 1 since 
        # there has to be at least one 
        # transformation
        res = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                
                # Base case we got there
                if word == endWord:
                    return res
                
                for pos in range(len(word)):
                    pattern = word[:pos] + "*" + word[pos + 1:]
                    for nei in adj_list[pattern]:
                        if nei not in seen:
                            seen.add(nei)
                            q.append(nei)
            
            # and for every round we have
            # gone 1 layer deep
            res += 1
        
        # if we never reach it then
        # it is automatically 0
        return 0