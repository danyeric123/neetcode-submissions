class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # first guarentee there is a solution
        if sum(gas) < sum(cost): return -1

        total = 0
        start = 0

        # if we find a potential starting point
        # then we know it is the answer since there
        # is only one solution
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                start = i + 1
        
        return start