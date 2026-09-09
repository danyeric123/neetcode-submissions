class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # you want to sort it first
        # so that you can predicably
        # take two people

        # This problem is similar to two 
        # pointer with target

        # If you do not want to sort,
        # then you can do count sort

        max_weight = max(people)

        counts = Counter(people)

        idx, num = 0, 1
        # go through all the counts
        # until we have all
        while idx < len(people):
            while counts[num] == 0:
                # only move to next num
                # if we exhausted all counts
                # or this is just empty
                num += 1

            people[idx] = num
            counts[num] -= 1
            idx += 1
        
        
        res, l, r = 0, 0, len(people) - 1
        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1
            if l <= r and remain >= people[l]:
                l += 1
        return res