class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        """
        You want to use a sliding window where you 
        move the left when it gets invalid
        but in this case, you are moving l with r
        so the window didn't change. Thus the window
        maintains the max we have seen
        """

        count = defaultdict(int)
        l = 0

        for r in range(len(fruits)):
            count[fruits[r]] += 1

            if len(count) > 2:
                # only move the l since
                # the window size doesn't
                # change
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    count.pop(fruits[l])
                l += 1

        # This gives us the max window
        # we have seen at the end
        return len(fruits) - l