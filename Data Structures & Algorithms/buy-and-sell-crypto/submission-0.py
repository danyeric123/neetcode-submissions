class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        smallest = float('inf')

        for p in prices:
            smallest = min(p, smallest)
            profit = max(profit, p - smallest)

        return profit