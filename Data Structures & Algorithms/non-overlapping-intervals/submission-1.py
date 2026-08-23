class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        For this problem you just need to keep track of how many
        times they overlap with the previous. You can sort by end
        or by start, but sorting by start means you need to keep 
        track of the earlier end
        """
        intervals.sort(key=lambda x: x[1])

        min_intervals = 0
        curr_end = intervals[0][1]

        for start,end in intervals[1:]:
            if start < curr_end:
                min_intervals += 1
            else:
                curr_end = end
        
        return min_intervals