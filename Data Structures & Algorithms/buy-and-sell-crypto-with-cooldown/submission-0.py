class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # this requires a decision tree and we can cut down
        # the repeated work by doing DP. Since decision trees usually 
        # mean DFS that is what we will do

        # (point at which I am, whether I am buying or selling) -> max_profit
        dp: dict[tuple[int, bool], int] = {} 

        def dfs(i: int, is_buying: bool) -> int:

            # Base cases
            if i >= len(prices):
                return 0
            
            if (i, is_buying) in dp:
                return dp[(i, is_buying)]
            
            no_op = dfs(i+1, is_buying)

            if is_buying:
                # since you bought that reduces the max profit
                # you can have from the decision tree afterwards
                buy = dfs(i + 1, not is_buying) - prices[i]
                dp[(i, is_buying)] = max(buy, no_op)
            else:
                # +2 since you are forced for the cooldown
                sell = dfs(i+2, not is_buying) + prices[i]
                dp[(i, is_buying)] = max(sell, no_op)

            return dp[(i, is_buying)]
        
        # Start with buying
        return dfs(0, True)