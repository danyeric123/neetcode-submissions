class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        l = res = 0
        for r in range(1, len(colors)):
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    res += neededTime[l]
                    # jump to r since we are keeping
                    # r but getting rid of l
                    l = r
                else:
                    # Do not need to shift anything
                    # since we keep l and r moves with loop
                    res += neededTime[r]
            else:
                # we do not need to worry about adjacents
                # so just move on
                l = r
        
        return res
            