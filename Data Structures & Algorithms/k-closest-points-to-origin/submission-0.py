class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # So I need to have the euclidean distances

        def euclidean_distance_to_origin(point: tuple[int,int])->int:
            x, y = point
            return x**2 + y**2
        
        return sorted(points, key=euclidean_distance_to_origin)[:k]