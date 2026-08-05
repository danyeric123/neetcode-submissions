class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        This is a two pointer where we 
        start at one end and the other
        and if the sum isn't big enough make
        left bigger, and if sum is too big
        then make right smaller

        At some point, you need to account for 
        off by one
        """

        l, r = 0, len(numbers) - 1

        while l < r:
            potential = numbers[l] + numbers[r]

            if potential > target:
                r -= 1
            if potential < target:
                l += 1
            
            if potential == target:
                return [l+1, r+1]