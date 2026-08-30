class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # instead of sorting we can keep track of the changes
        # over the range of stops

        l, r = float("inf"), float("-inf")
        for _, start,end in trips:
            l = min(l, start)
            r = max(r, end)

        stop_range = r - l + 1

        pass_change = [0] * (stop_range+1)

        for num_pass, start,end in trips:
            # record when they come on and go off
            # offset by the first stop location
            pass_change[start - l] += num_pass
            pass_change[end - l] -= num_pass

        curr_pass = 0
        for change in pass_change:
            curr_pass += change
            if curr_pass > capacity:
                return False

        return True