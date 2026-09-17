class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        # There are two ways to do this problem
        # either we do a line sweep or two pointers
        # we also have to assume that the intervals
        # within a list are disjointed and cannot overlap
        # each other

        i = j = 0
        
        res =[]
        
        while i < len(firstList) and j < len(secondList):
            first_start, first_end = firstList[i]
            second_start, second_end = secondList[j]
            
            if first_start <= second_end and second_start <= first_end:
                # if they overlap, which means the start of one
                # has to be before the end of the other (or equal)
                res.append([max(first_start, second_start), min(first_end, second_end)])
                
            # whichever ends first then
            # move to the next interval
            # in that list
            if first_end < second_end:
                i += 1
            else:
                j+=1
                
        return res