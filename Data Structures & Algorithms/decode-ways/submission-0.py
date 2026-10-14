class Solution:
    def numDecodings(self, s: str) -> int:
        # This can be space optimized to just have 
        # the current dp, dp1 and dp2
        dp = [0] * (len(s) + 1)
        # We need to initalize to 1
        dp[len(s)] = 1

        # We can work backwards and build up
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                # We can assume there is 
                # one way to decode
                dp[i] = dp[i+1]
            
            # Now we want to see if there are 
            # others
            if i + 1 < len(s) and (
                s[i] == "1"  or
                s[i] == "2" and s[i+1] in "0123456"
            ):
                dp[i] += dp[i+2]
        
        return dp[0]