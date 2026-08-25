class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        This is a window problem where you move the 
        left pointer when we see repeating characters
        """

        l = r = 0
        max_size = 0

        seen = set()

        for r, letter in enumerate(s):
            while letter in seen:
                # remove from left until 
                # the new letter is new
                seen.remove(s[l])
                l += 1

            seen.add(letter)
            max_size = max(r-l+1, max_size)
        
        return max_size