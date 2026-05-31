class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        This is a two pointer where we move the left if
        it becomes smaller than r (meaning we want a bigger one)
        otherwise we move right, or do the opposite
        The key idea is keep the higher height and move the smaller
        height
        """
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            area = (r-l)*min(height[l], height[r])
            max_area = max(area, max_area)

            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        
        return max_area