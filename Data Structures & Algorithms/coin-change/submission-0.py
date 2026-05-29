class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bottom up solution
        # create a dp array of the number of coins
        # to get to this amount

        dp = [0] + [float("inf")] * amount

        for i in range(1, amount+ 1):
            for coin in coins:
                # check if we can use this coin
                # and if so will this be the least 
                # number of coin possibilities
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        
        return dp[-1] if dp[-1] != float("inf") else -1