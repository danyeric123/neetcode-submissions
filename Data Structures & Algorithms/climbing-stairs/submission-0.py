class Solution:
    def climbStairs(self, n: int) -> int:
        if n in (1,2):
            # Base case where it is 
            # either one or two steps
            return n

        steps_1, steps_2 = 1, 2

        for _ in range(1, n-1):
            # we do n-1 since we want to
            # get to allow two steps to
            # land us exactly on n
            tmp = steps_2
            steps_2 = steps_1 + steps_2
            steps_1 = tmp
        
        return steps_2
            