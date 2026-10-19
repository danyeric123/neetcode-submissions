class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l = 1
        r = min(ranks) * cars**2
        res = 0

        def can_repair(time):
            total_cars_repaired = 0
            for rank in ranks:
                cars_repaired = int((time/rank) ** 0.5)
                total_cars_repaired += cars_repaired
                if total_cars_repaired >= cars: return True
            
            return False

        while l <= r:
            mid = (l+r) //2
            if can_repair(mid):
                # maybe there is a smaller time
                r = mid - 1
                res = mid
            else:
                l = mid + 1

        return res
