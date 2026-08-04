class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}

        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in compliments:
                return [compliments[compliment], i]
            
            compliments[num] = i
        
        return []