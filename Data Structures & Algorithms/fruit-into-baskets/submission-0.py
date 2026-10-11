class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        """
        You want to use a sliding window where you 
        pop off the left when there are more than two
        """

        count = defaultdict(int)
        l, total, res = 0, 0, 0
        for r in range(len(fruits)):
            count[fruits[r]] += 1
            total += 1

            while len(count) > 2:
                # remove from left
                # until we have exactly
                # two fruits
                fruit = fruits[l]
                count[fruit] -= 1
                total -= 1
                l += 1

                if not count[fruit]:
                    # remove so count is correct
                    count.pop(fruit)

            res = max(res, total)
        
        return res