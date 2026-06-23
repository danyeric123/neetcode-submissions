class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        For this solution you need to pick a point and then 
        go out from there like you would do with palindrome checking
        in general
        """

        self.count = 0

        def check(i: int, j: int) -> None:
            while (
                0 <= i < len(s) and
                0 <= j < len(s) and
                s[i] == s[j]
            ):
                self.count += 1
                # move out by moving
                # left on i and right on j
                i -= 1
                j += 1

        for i in range(len(s)):
            # Check both where mid is 1 and 2
            check(i, i)
            check(i, i+1)
        
        return self.count