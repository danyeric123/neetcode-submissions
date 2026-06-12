# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None
        
        res = ListNode(0)
        curr = res
        min_heap = []

        for i, l in enumerate(lists):
            if l is None:
                continue
            
            heapq.heappush(min_heap, (l.val, i))
        
        while min_heap:
            _, i = heapq.heappop(min_heap)

            curr.next = lists[i]
            curr = curr.next

            if lists[i].next:
                heapq.heappush(min_heap, (lists[i].next.val, i))
                lists[i] = lists[i].next
        
        return res.next

