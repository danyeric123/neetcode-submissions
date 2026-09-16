class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        # There are two ways to do this problem
        # either we do a line sweep or two pointers
        # we also have to assume that the intervals
        # within a list are disjointed and cannot overlap
        # each other

        mapping = defaultdict(int)

        for start, end in firstList:
            mapping[start] += 1
            # Need to do +1 since it is a closed interval
            mapping[end + 1] -= 1
        
        for start, end in secondList:
            mapping[start] += 1
            mapping[end +1] -= 1
        
        res = []
        active = 0

        prev = None

        for num in sorted(mapping):
            if active == 2:
                # if we get two then there was
                # a previous overlap that just ended
                # hence minus one
                res.append([prev, num - 1])
            active += mapping[num]
            prev = num
        
        return res