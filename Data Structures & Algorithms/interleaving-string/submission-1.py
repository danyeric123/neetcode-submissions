class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # The point here is that it needs to be in the same order
        # of the original string so we go through the order of s3
        # and figure out which it matches and then if both s1 and s2
        # has said char then that is where the backtracking can happen

        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1)+ 1)]

        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
        
        return dp[0][0]
                