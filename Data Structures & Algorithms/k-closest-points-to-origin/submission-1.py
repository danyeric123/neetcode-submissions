class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # So I need to have the euclidean distances

        def euclidean_distance_to_origin(point: tuple[int,int])->int:
            x, y = point
            return x**2 + y**2
        
        # I can either sort it based off of that
        # return sorted(points, key=euclidean_distance_to_origin)[:k]

        # or I can use a heap and using a heap 
        # might be better since sorting is for all
        # as opposed to k log (N) for k < N

        min_heap = []

        for point in points:
            heapq.heappush(min_heap, (-euclidean_distance_to_origin(point), point))
            if len(min_heap) > k:
                # You pop off the heap 
                # so that the heap is always k
                # and it will maintain closest
                # by the properties of a heap
                heapq.heappop(min_heap)
        
        return [point for _, point in min_heap]