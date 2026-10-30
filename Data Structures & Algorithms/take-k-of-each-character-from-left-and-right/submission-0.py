class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        """
        Your first thought might be to do two pointer
        and then maybe backtrack with memoization, but
        if we think about this in reverse we can do sliding window

        Reverse thinking: try to find the maximum window of elements
        you do not choose, and maintain the counts by having the current
        count of the outside window and the total count
        Shift left pointer when lose the count you need for a, b, or c
        """

        outside = [s.count(c) for c in "abc"]

        if min(outside) < k: return -1

        left = res = 0

        for right, c in enumerate(s):
            char_num = ord(c) - 97
            outside[char_num] -= 1

            while outside[char_num] < k:
                # Shift the window left since we lost the 
                # count
                outside[ord(s[left]) - 97] += 1   
                left += 1
            
            # maximum window is the minimum removed
            res = max(res, right - left + 1)

        # return the window
        return len(s) - res