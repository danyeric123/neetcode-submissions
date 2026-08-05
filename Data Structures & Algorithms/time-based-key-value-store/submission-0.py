class TimeMap:

    def __init__(self):
        self._store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        """
        We will need to search for the closest
        value to what we are looking for
        """

        if not self._store[key]: return ""

        values = self._store[key]

        l, r = 0, len(values) - 1

        res = ""

        # We do equal to because
        # both ends are possible
        # And we are looking for 
        # most feasible
        while l <= r:
            mid = (l + r) //2
            possible_t, value = values[mid]

            if timestamp >= possible_t:
                # Move to the right half since there
                # could be a closer value to timestamp
                # but set res to value since we could be wrong
                res = value
                l = mid + 1
            
            if timestamp < possible_t:
                r = mid - 1
        
        return res
                


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)