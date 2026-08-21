class MinStack:

    def __init__(self):
        """
        We need to have two stacks
        one to store the value and the
        other to store where the minimum
        up to that point is in the stack
        """
        self._stack = []
        self._min_stack = []

    def push(self, value: int) -> None:
        self._stack.append(value)

        if not self._min_stack or self._stack[self._min_stack[-1]] > value:
            # keep track of where the minimum is
            self._min_stack.append(len(self._stack) - 1)

    def pop(self) -> None:
        del self._stack[-1]

        if self._min_stack[-1] == len(self._stack):
            # if the one we just pop was the minimum 
            # remove it
            del self._min_stack[-1]
        

    def top(self) -> int:
        return self._stack[-1]
        

    def getMin(self) -> int:
        return self._stack[self._min_stack[-1]]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()