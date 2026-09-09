class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # you want to sort it first
        # so that you can predicably
        # take two people

        # This problem is similar to two 
        # pointer with target

        people.sort()
        boats = 0

        l, r = 0, len(people) -1

        while l <= r:

            if people[l] + people[r] <= limit:
                # if we can use both then we 
                # can move left
                l += 1
            # otherwise at minimum we can fit the 
            # larger of the two
            boats += 1
            r -= 1
        
        return boats
