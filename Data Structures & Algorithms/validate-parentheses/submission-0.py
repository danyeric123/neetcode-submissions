class Solution:
    def isValid(self, s: str) -> bool:
        pairings = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []

        for char in s:
            if char not in pairings:
                # if it is not a closing then add to stack
                # since we will need to find a closing for it
                stack.append(char)
                continue
            
            # otherwise we hit a closing parentheses
            
            # Either we have nothing to pair the closing with
            # because the stack is empty 
            # or the top of the stack will not match this parentheses
            if len(stack) == 0 or pairings[char] != stack[-1]:
                return False
            
            stack.pop()
        
        # We need to make sure that the stack is emptied
        # or else there clearly was an opening parentheses
        # that wasn't matched
        return len(stack) == 0