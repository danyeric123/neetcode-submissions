class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        We want to go through the intervals and then when we have an 
        opportunity to merge we merge the new one
        """

        res = []

        for i, interval in enumerate(intervals):
            start_new, end_new = newInterval
            start, end = interval

            # if the new interval ends
            # before the start of this one
            # then we can assume everything 
            # from this current interval and 
            # onwards can be appended onto what 
            # we have so far
            if end_new < start:
                res.append(newInterval)
                return res + intervals[i:]
            
            # if the new interval has not
            # even started yet
            if start_new > end:
                res.append(interval)
            
            # Otherwise the new interval overlaps
            # somehow, and we just need to figure out what
            # the new range should be
            else:
                newInterval = (
                    min(start_new, start),
                    max(end_new, end)
                )

        # Append at the end of loop since it might not have 
        # been added yet    
        res.append(newInterval)
        
        return res