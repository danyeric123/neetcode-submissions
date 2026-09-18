from heapq import heappush, heappop, heapify
class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ""

        counts = Counter(s)

        # we want to be greedy with this and take the most frequent 
        # before the less frequent
        heap = [(-count, char) for char, count in counts.items()]
        heapify(heap)

        # We need to keep track of 
        # previously used char so we
        # maintain no two adjacent
        on_hold = None

        while heap or on_hold:
            if on_hold and not heap:
                # when we have only
                # the hold and the heap is
                # empty then we have a repeat
                return ""

            count, char = heappop(heap)

            res += char
            count += 1

            if on_hold:
                # if we have something
                # on hold then let's add it back
                heappush(heap, on_hold)
                on_hold = None
            
            if count != 0:
                # if the count of the current 
                # is not zero then we put this on hold
                on_hold = (count, char)

        
        return res

