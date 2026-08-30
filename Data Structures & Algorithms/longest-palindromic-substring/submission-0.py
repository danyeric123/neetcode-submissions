class Solution:
    def longestPalindrome(self, s: str) -> str:
        # You want to determine whether something is a palindrome
        # but you want to do this starting from each point in the string
        # this is faster than just taking two indices and checking each time

        def get_palindrome(l: int, r: int) -> int:
            # pass two indices and then move out to account
            # for even palindromes
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            # need to do l + 1 since l can go negative
            return s[l+1:r]
        
        res = ""

        for i in range(len(s)):
            # You want to see odd and even palindromes
            odd_cand = get_palindrome(i,i)
            even_cand = get_palindrome(i, i+1)
            res = max(
                odd_cand,
                even_cand,
                res,
                key=len
            )
        
        return res