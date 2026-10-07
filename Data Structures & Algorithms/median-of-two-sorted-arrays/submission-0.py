class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # When we combine the two arrays (theoretically)
        # then we know that the left partition should be equal
        # to half the combined. That means part of nums1 and nums2
        # should equal half the combined

        if len(nums2) < len(nums1):
            # swap so that nums1 is always smaller
            # which we use to compute
            nums1, nums2 = nums2, nums1
        
        total = len(nums2) + len(nums1)
        half = total // 2

        # This is the left and right 
        # of the smaller array and we can 
        # figure out the other one by doing the math
        l, r = 0, len(nums1) - 1

        # since there will always be a middle
        # we can just run until we find it
        while True:
            i = (l + r) // 2
            j = half - i - 2

            nums1_left = nums1[i] if i >= 0 else float("-inf")
            nums1_right = nums1[i + 1] if (i + 1) < len(nums1) else float("inf")
            nums2_left = nums2[j] if j >= 0 else float("-inf")
            nums2_right = nums2[j + 1] if (j + 1) < len(nums2) else float("inf")

            # partition is correct and we have them match
            # correctly
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if total % 2:
                    # if one median
                    return min(nums1_right, nums2_right)
                
                return (
                    max(nums1_left, nums2_left) +
                    min(nums1_right, nums2_right)
                ) / 2
            
            if nums1_left > nums2_right:
                r = i -1
            else:
                l = i + 1