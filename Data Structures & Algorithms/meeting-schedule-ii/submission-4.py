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
        Another way of looking at this is 
        by going through time and seeing what
        meetings are running at that time and 
        the max number of meetings are the min
        we need
        """

        meetings = defaultdict(int)

        for interval in intervals:
            meetings[interval.start] += 1
            meetings[interval.end] -= 1

        prev = res = 0

        for t in sorted(meetings.keys()):
            prev += meetings[t]
            res = max(res, prev)
        
        return res