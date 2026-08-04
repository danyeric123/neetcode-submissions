class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        The intuition is that the max number of hours
        would be the maximum size pile
        It would not make sense to go from 1 to max
        instead we should search for the minimum number
        of hours. Once we hit that it is not possible anymore
        then exit and return res
        """

        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = (l + r) //2

            time = 0

            # Some math for rate
            for pile in piles:
                time += math.ceil(pile/mid)

            # if too big then move to right half
            # since you want a faster speed
            if time > h:
                l = mid + 1

            # if smaller than or equal to h then 
            # set res and go to the left half since
            # you want a slower speed if possible
            else:
                res = mid
                r = mid - 1


        return res