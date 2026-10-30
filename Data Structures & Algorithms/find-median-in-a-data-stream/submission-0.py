class MedianFinder:

    def __init__(self):
        self._small, self._large = [], []

    def addNum(self, num: int) -> None:
        if self._large and num > self._large[0]:
            heapq.heappush(self._large, num)
        else:
            heapq.heappush(self._small, -1 * num)

        if len(self._small) > len(self._large) + 1:
            val = -1 * heapq.heappop(self._small)
            heapq.heappush(self._large, val)
        if len(self._large) > len(self._small) + 1:
            val = heapq.heappop(self._large)
            heapq.heappush(self._small, -1 * val)

    def findMedian(self) -> float:
        if (len(self._small) + len(self._large)) % 2 == 0:
            return (
                self._small[0] * -1 + self._large[0]
            ) / 2
        
        return self._small[0] * -1 if len(self._small) > len(self._large) else self._large[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()