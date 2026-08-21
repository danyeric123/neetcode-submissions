class LRUCache:
    """
    We can do this in two different ways:
    1. OrderedDict where we evict the last one, which dicts are now ordered
    2. LinkedList where we have to perform inserts and removals
    """
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = {}

    def get(self, key: int) -> int:
        if key not in self._cache: 
            return -1
        
        val = self._cache[key]
        # move it up to the most recent
        del self._cache[key]
        self._cache[key] = val

        return val
        

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            del self._cache[key]
        
        self._cache[key] = value

        # handle when we are over capacity
        if len(self._cache) > self._capacity:
            # first key is the oldest since it was
            # the first inserted
            oldest_key = next(iter(self._cache))
            del self._cache[oldest_key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)