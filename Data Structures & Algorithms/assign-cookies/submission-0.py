class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i = j = 0

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                # This one can be satisfied
                i += 1
            # Either we used a cookie up or 
            # not big enough
            j += 1
        
        # i then represents the number of 
        # kids with cookies
        return i
