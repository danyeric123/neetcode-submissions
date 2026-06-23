class Solution:
    def rob(self, nums: List[int]) -> int:
        max_two_houses_before = 0    # Max money if we consider houses up to i-2
        max_one_house_before = 0     # Max money if we consider houses up to i-1

        for current_house in nums:
            current_max = max(
                current_house + max_two_houses_before,
                max_one_house_before
            )
            max_two_houses_before = max_one_house_before
            max_one_house_before = current_max
        
        return max_one_house_before