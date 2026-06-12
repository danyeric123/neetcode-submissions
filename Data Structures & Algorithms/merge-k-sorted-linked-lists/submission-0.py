# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """This is O(N*logK) since we go through the list k times
        and this is a divide and conquer algorithm"""

        if not lists:
            return None

        while len(lists) > 1: # continue to merge them until one remains
            merged_lists = []
            for i in range(0,len(lists), 2):
                # go through every list pairwise
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                merged_lists.append(self.merge_lists(l1, l2))
            
            lists=merged_lists
        
        return lists[0]

    
    def merge_lists(self, list_1: List[Optional[ListNode]], list_2: Optional[List[Optional[ListNode]]]) -> List[Optional[ListNode]]:
        # This is now just merge two sorted lists
        dummy = ListNode()

        # we need a tail to keep track of the end we 
        # are appending to
        tail = dummy

        while list_1 and list_2:

            if list_1.val < list_2.val:
                tail.next = list_1
                list_1 = list_1.next
            else:
                tail.next = list_2
                list_2 = list_2.next
            
            tail = tail.next
        
        if list_1:
            tail.next =list_1
        if list_2:
            tail.next = list_2
        
        return dummy.next

