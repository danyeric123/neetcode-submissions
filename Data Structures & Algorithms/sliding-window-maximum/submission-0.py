class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        if we have a monotonic decreasing we know that
        the front of the queue is the largest
        """
        output = []
        q = deque()
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                # if left is out of bounds
                q.popleft()
            
            if (r + 1) >= k:
                output.append(nums[q[0]])
                # once we add then we shift the 
                # window
                l += 1
            r += 1
        
        return output