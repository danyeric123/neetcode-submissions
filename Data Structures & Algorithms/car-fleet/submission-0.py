class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        We want to go in reverse order
        and see when the next car will
        catch up to the previous one
        """

        pairs = [(p, s) for p,s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = [] 

        for p, s in pairs:
            # Calculate what time this car will reach the target
            stack.append((target - p) / s)

            # If this car arrives at the same time or sooner than
            # the one in front, it means it's fast enough to catch up.
            # But since it can't pass, it merges into the fleet ahead
            # and the slower car's time dictates the fleet.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # Remove the faster car at the top of the stack
                # since it merges into the fleet ahead
                stack.pop()
        
        return len(stack)