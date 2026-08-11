class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        You want the most frequent in the window to remain
        and replace the rest. And if the replacement is less
        than or equal to k then it is a valid window, otherwise 
        we want to move left
        """

        count = defaultdict(int)

        l = 0
        max_freq = 0
        res = 0

        for r, char in enumerate(s):
            count[char] += 1

            max_freq = max(max_freq, count[char])

            # check if it is a valid window 
            if (r - l + 1) - max_freq > k:
                # evict the left if not valid
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        
        return res