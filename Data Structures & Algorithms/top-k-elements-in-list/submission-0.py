class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]
        
        # by definition using the buckets gives you a sort
        # since we go from 0 -> len(nums)
        for num, count in c.items():
            buckets[count].append(num)
        
        res = []

        # by going in reverse you go from most common
        # to least
        for bucket in buckets[::-1]:
            res.extend(bucket)

            # once we have k or more then we are good
            # since we took the most common
            # but it can be more since there can be multiple 
            # items in one bucket
            if len(res) >= k:
                return res[:k]
