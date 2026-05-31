class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack: list[tuple[int, int]] = [] # temp, int pairs

        for i, temp in enumerate(temperatures):
            # as long as the stack is not empty and 
            # the top of the stack's temp is less than
            # current temp
            while stack and temp > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                # get the distance from the temp to curent
                # since we only care about the first time 
                # there is a greater temp
                res[stack_index] = i - stack_index
            
            stack.append((temp, i))
        
        return res
            