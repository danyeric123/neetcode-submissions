class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        We work backwards by thinking about what happens 
        if a given number is the "last" to be popped, thus 
        working backwards. And since this is a DP problem
        we do DFS
        """

        nums = [1] + nums + [1]
        dp = {}

        def dfs(l: int, r: int) -> None:
            if l > r: return 0

            if (l, r) in dp: return dp[(l,r)]

            dp[(l,r)] = 0

            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r+1]
                coins += dfs(l, i -1) + dfs(i+1, r)
                dp[(l,r)] = max(dp[(l,r)], coins)
            
            return dp[(l,r)]

        return dfs(1, len(nums) - 2)
