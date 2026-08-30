class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # sort by starting point
        trips.sort(key=lambda t: t[1])
        min_heap = [] # heap has destination and number of pass coming on
        curr_pass = 0

        for num_pass, start, end in trips:

            # first see if any passengers got off at or before
            # this pickup
            while min_heap and min_heap[0][0] <= start:
                curr_pass -= heapq.heappop(min_heap)[1]
            
            curr_pass += num_pass

            # if at any point we have gone over
            # the number of passengers possible
            if curr_pass > capacity:
                return False
            
            heapq.heappush(min_heap, (end, num_pass))
        

        # if we never went over capacity then
        # we can do the trip
        return True