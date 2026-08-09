class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for j in range(len(word2) + 1):
            # the len of the subproblem
            dp[len(word1)][j] = len(word2) - j
        
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i
        
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                # We do bottom up to build it up

                # Base case, they are equal
                # so nothing to be done
                # and just continue with what we had before
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    # we need to do some operation
                    # plus the minimum of the options
                    dp[i][j] = 1 + min(
                        dp[i+1][j], # delete case
                        dp[i][j+1], # insert case
                        dp[i +1][j+1] # replace
                    )
                
        
        return dp[0][0]