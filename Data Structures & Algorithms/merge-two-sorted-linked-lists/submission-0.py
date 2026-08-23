# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        l1, l2 = list1, list2


        while l1 or l2:
            l1_val = l1.val if l1 else float("inf")
            l2_val = l2.val if l2 else float("inf")
            if l1_val < l2_val:
                curr.next = ListNode(l1_val)
                l1 = l1.next
            else:
                curr.next = ListNode(l2_val)
                l2 = l2.next
            
            curr = curr.next
        
        return dummy.next