class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                # we stop here since we have
                # right and left in sorted order
                break
            
            m = (l + r) // 2
            # keep track of mid since it could 
            # be minimum
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                # this tells us we are in
                # the left *sorted* portion
                # which means we want the right
                # for minimum
                l = m + 1
            else:
                r = m - 1
        
        return res