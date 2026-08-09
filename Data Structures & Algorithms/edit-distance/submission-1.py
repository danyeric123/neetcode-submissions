class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Space optimized is always just two rows

        m, n = len(word1), len(word2)

        # make sure that m is bigger
        if m < n:
            m, n = n,m
            word1, word2 = word2, word1
        
        dp = [0] * (n+1)
        next_dp = [0] * (n+1)

        for j in range(n+1):
            # Go through bottom row
            dp[j] = n - j
        
        for i in range(len(word1) - 1, -1, -1):
            # first initialize next rightmost
            next_dp[n] = m - i

            for j in range(len(word2) - 1, -1, -1):
                # We do bottom up to build it up

                # Base case, they are equal
                # so nothing to be done
                # and just continue with what we had before
                if word1[i] == word2[j]:
                    next_dp[j] = dp[j + 1]
                else:
                    # we need to do some operation
                    # plus the minimum of the options
                    next_dp[j] = 1 + min(
                        dp[j], # delete case
                        next_dp[j+1], # insert case
                        dp[j+1] # replace
                    )
            
            # then current becomes what was next_dp
            dp = next_dp[:]
                
        
        return dp[0]