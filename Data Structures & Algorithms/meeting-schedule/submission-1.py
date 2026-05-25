"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals: return True
        intervals.sort(key=lambda x: x.start)
        curr_start, curr_end = intervals[0].start, intervals[0].end
        for interval in intervals[1:]:
            # The previous meetings ending is after the
            # start of the next one
            if curr_end > interval.start:
                return False
            curr_start, curr_end = interval.start, interval.end
        
        return True