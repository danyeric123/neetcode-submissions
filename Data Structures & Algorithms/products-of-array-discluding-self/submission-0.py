class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1

        for i, num in enumerate(nums):
            # set the current position in res
            # to prefix so can keep track of multiplication
            # of everything to the left
            res[i] = prefix

            # Keep track of prefix which will be all
            # of the left
            prefix *= num
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            # multiply what is to the right
            # and when you do that you are multiplying 
            # postfix by prefix
            res[i] *= postfix

            # Keep track of postfix, which will be
            # multiplication of all of right
            postfix *= nums[i]
        
        return res