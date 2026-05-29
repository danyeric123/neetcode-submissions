import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        This uses quick select, which is similar to quicksort
        basically we choose a pivot and put numbers larger to 
        right and numbers smaller to left and if they equal the pivot
        then that is mid

        if the left has more or the same as k, then the number must 
        be within left
        if the left and mid are smaller than k, then right much have it
        and we want to find the -th of what is left after L+M is removed
        Otherwise, left + mid is equal to k, which means mid has it
        """

        if not nums: return 

        pivot = random.choice(nums)
        right = [num for num in nums if num < pivot]
        left = [num for num in nums if num > pivot]
        mid = [num for num in nums if num == pivot]

        l, m = len(left), len(mid)

        if l + m < k:
            return self.findKthLargest(right, k - l - m)
        
        if l >= k:
            return self.findKthLargest(left, k)
        
        return mid[0]