"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        The idea of using a min heap is that we want
        the first room available to pop out
        and then keep track of the number of meetings at
        the end
        """

        intervals.sort(key=lambda i: i.start)

        # heap of end times
        # so we pop as soon as it is end time
        min_heap = []

        for interval in intervals:
            # if there are still meetings
            # and there is a meeting room now available
            # i.e. top of heap (earliest end time) is at 
            # or before start of this meeting
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            
            # No matter what, we are using a meeting room
            heapq.heappush(min_heap, interval.end)
                
        return len(min_heap)


