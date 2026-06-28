import functools
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

        @functools.cache
        def dfs(l: int, r: int) -> None:
            if l > r:
                return 0

            return max(
                nums[l - 1] * nums[i] * nums[r + 1] + dfs(l, i - 1) + dfs(i + 1, r)
                for i in range(l, r + 1)
            )

        return dfs(1, len(nums) - 2)
