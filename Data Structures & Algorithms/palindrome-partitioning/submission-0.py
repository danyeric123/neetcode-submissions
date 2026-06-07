class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        You will need a check for is_palindrome 

        You need to view this as different ways to 
        break up the string. So we need to have different
        decisions on how to break it up. Hence it is a decision tree,
        which involves DFS
        """

        res, partition = [], []

        # This is a decision tree around 
        # where we are partitioning the string
        # so it involves backtracking
        def dfs(i: int) -> None:
            if i == len(s):
                # At this point we have gone through the whole string
                # and now we want to add the result of partitioning from 
                # before
                res.append(partition.copy())
                return
            
            for j in range(i, len(s)):
                if self.is_palindrome(s, i, j):
                    partition.append(s[i:j+1])
                    dfs(j + 1)
                    # Here is where we backtrack
                    # and if we never end up at the 
                    # end with a clear partition with 
                    # palindrome, then it is undone completely
                    partition.pop()
        
        dfs(0)
        return res

    
    def is_palindrome(self, s: str, l: str, r: str) -> bool:
        
        while l < r:
            if s[l] != s[r]:
                return False
            
            l, r = l +1, r -1
        
        return True