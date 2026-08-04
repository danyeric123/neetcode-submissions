class Solution:

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # We sort so that we can go through all the negatives first
        # because there has to be negative numbers to get 0
        nums.sort()
        self.res = []

        for i, num in enumerate(nums):
            
            # Once we hit positive numbers
            # then we went through all possibilities
            # since we need negative and positive
            if num > 0:
                break
            
            # We have to do the first one since we haven't
            # tried any and we do not want two duplicates
            if i == 0 or num != nums[i-1]:
                self.two_sum(i, nums)
            
        # Once we broke, then all we need is the res
        return self.res
    
    def two_sum(self, curr_index: int, nums: list[int]) -> None:
        l, r = curr_index + 1, len(nums) - 1

        while l < r:
            potential_sum = nums[curr_index] + nums[l] + nums[r]

            if potential_sum == 0:
                self.res.append((nums[curr_index], nums[l], nums[r]))

                l += 1
                r -= 1

                while l < r and nums[l] == nums[l-1]:
                    l += 1
            
            if potential_sum > 0:
                r -= 1
            if potential_sum < 0:
                l += 1
        
