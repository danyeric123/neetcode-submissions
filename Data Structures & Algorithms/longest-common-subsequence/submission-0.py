class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+ 1)]

        # We figure out the solution bottom up
        # That is, starting from the end of the strings to the beginning
        # This is since that will be the smallest with no further subproblems
        for i in range(len(text1) -1, -1, -1):
            for j in range(len(text2) -1, -1, -1):
                if text1[i] == text2[j]:
                    # Since this char is the same, then add 1 to the diagnol place
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    # Otherwise, find the max between the row down and the col to the right
                    # That is, we look at the max between considering with i vs with j
                    dp[i][j] = max(dp[i][j+1],dp[i+1][j])
        
        return dp[0][0]