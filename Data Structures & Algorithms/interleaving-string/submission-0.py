class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # The point here is that it needs to be in the same order
        # of the original string so we go through the order of s3
        # and figure out which it matches and then if both s1 and s2
        # has said char then that is where the backtracking can happen

        # Memoization
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}

        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in dp:
                return dp[(i, j)]

            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                dp[(i, j)] = True
                return True

            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                dp[(i, j)] = True
                return True

            dp[(i, j)] = False
            return False

        return dfs(0, 0)