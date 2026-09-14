class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = Counter(arr)

        max_lucky = -1

        for integer, count in counts.items():
            if integer == count:
                max_lucky = max(integer, max_lucky)
        
        return max_lucky