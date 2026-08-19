class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def can_ship(cap: int) -> bool:
            ships, curr_cap = 1, cap

            for w in weights:
                if curr_cap - w < 0:
                    # we cannot fit on ship
                    ships += 1
                    if ships > days:
                        return False
                    # reset cap since it is a
                    # new ship
                    curr_cap = cap
                
                curr_cap -= w
            
            return True
                

        while l <= r:
            mid = (l+r) //2

            if can_ship(mid):
                res = min(res, mid)
                # check left half if there
                # is a lower bound
                r = mid - 1
            else:
                l = mid + 1
        
        return res