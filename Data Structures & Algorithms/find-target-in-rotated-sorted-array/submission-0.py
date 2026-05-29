class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Searches for target in a rotated sorted array and returns its index if found, -1 otherwise.
        
        This algorithm handles arrays that were initially sorted in ascending order,
        then rotated at some pivot point. For example: [4,5,6,7,0,1,2] was originally
        [0,1,2,4,5,6,7] before being rotated.
        """

        l, r = 0, len(nums) -1 

        while l <= r:
            mid = (l + r) //2 

            if nums[mid] == target:
                return mid
            
            # determine which half is sorted
            if nums[l] <= nums[mid]:
                # we know that the left half is sorted
                # so let's see if target is in left half
                # or outside it
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    # it is outside of left half
                    # so let's look in right
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1

            