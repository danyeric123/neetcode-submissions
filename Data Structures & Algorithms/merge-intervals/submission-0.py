class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # We need to make sure they are sorted
        intervals.sort()

        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = merged[-1][1]

            # We try and see if there is any overlap
            # and if there is take whichever has the 
            # latest end
            if start <= last_end:
                merged[-1][1] = max(last_end, end)
            else:
                merged.append([start,end])
        
        return merged