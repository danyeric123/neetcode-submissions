# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        We can either do divide and conquer like merge sort
        or we can think in terms of a heap

        In either case, we would have O(N * log k)
        """
        
        if not lists:
            return None
        
        if len(lists) == 1: return lists[0]
        
        dummy = curr = ListNode(0)
        min_heap = []

        for i, l in enumerate(lists):
            if l is None:
                continue
            
            # Push the value and the index of the list
            heapq.heappush(min_heap, (l.val, i))
        
        
        while min_heap:
            # grab the lowest value in the heap
            _, i = heapq.heappop(min_heap)
            curr.next = lists[i]
            
            # Need to advance whether or not
            # the list has anything
            curr = curr.next

            # if we hit the end of the list
            # then just move on
            if not lists[i].next:
                continue

            # Push onto heap the next in line
            lists[i] = lists[i].next
            heapq.heappush(min_heap, (lists[i].val, i))

        
        return dummy.next
