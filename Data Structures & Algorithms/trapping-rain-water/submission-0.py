class Solution:
    def trap(self, heights: List[int]) -> int:
        """
        This is a sliding window problem
        The key here is that we want max left and max right
        since that will determine the size of the container
        with the minimum of the two determining the limit (see image)

        the amount you trap is min(l, r) - height[i]
        """

        if not heights: return 0

        l, r = 0, len(heights) - 1
        max_l, max_r = heights[l], heights[r]
        res = 0

        while l < r:
            # move before calculating so 
            # we make sure to calculate when 
            # l and r meet
            if max_l < max_r:
                l += 1
                max_l = max(max_l, heights[l])
                res += max_l - heights[l]
            else:
                r -= 1
                max_r = max(max_r, heights[r])
                res += max_r - heights[r]
        
        return res