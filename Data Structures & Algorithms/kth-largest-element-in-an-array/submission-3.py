import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        This uses quick select, which is similar to quicksort
        basically we choose a pivot and put numbers larger in 
        greater and numbers smaller in lesser and if they equal 
        the pivot then that is mid

        if greater has more or the same as k, then the number must 
        be within greater
        if greater and mid are smaller than k, then lesser must have it
        and we want to find the -th of what is left after G+M is removed
        Otherwise, greater + mid is equal to k, which means mid has it
        """

        if not nums: return 

        pivot = random.choice(nums)
        lesser = [num for num in nums if num < pivot]
        greater = [num for num in nums if num > pivot]
        mid = [num for num in nums if num == pivot]

        g, m = len(greater), len(mid)

        if g + m < k:
            return self.findKthLargest(lesser, k - g - m)
        
        if g >= k:
            return self.findKthLargest(greater, k)
        
        return mid[0]