class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob1(nums: list[int]) -> int:
            rob_1, rob_2 = 0, 0

            for n in nums:
                # Either you can rob current and two before
                # or skip current house and just rob one before
                rob_1, rob_2 = rob_2, max(n + rob_1, rob_2)
            
            return rob_2

        # you need nums[0] in the case where there is only one element
        return max(nums[0], rob1(nums[:-1]), rob1(nums[1:]))