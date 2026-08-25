from heapq import heapify, heappop, heappush

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._min_heap, self._k = nums, k
        heapify(self._min_heap)

        # We want to just keep the top k
        # since the rest does not matter
        # for this problem
        while len(self._min_heap) > k:
            heappop(self._min_heap)

    def add(self, val: int) -> int:
        heappush(self._min_heap, val)

        if len(self._min_heap) > self._k:
            heappop(self._min_heap)
        
        # We get the bottom since that
        # will be the kth largest
        return self._min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)