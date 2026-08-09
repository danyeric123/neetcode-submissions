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
        
        if not lists or len(lists) == 0:
            return None
        
        if len(lists) == 1: return lists[0]
        
        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                # get lists pairwise

                l1 = lists[i]
                l2 = lists[i+1] if (i+ 1) < len(lists) else None

                merged_lists.append(self.merge_lists(l1, l2))
            
            lists = merged_lists
        
        return lists[0]
    
    def merge_lists(self, l1: ListNode, l2: ListNode | None) -> ListNode:
        if not l2: return l1

        curr = dummy = ListNode(0)

        while l1 and l2:
            
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            
            curr = curr.next
        
        if l1:
            curr.next = l1
        
        if l2:
            curr.next = l2
        
        return dummy.next

