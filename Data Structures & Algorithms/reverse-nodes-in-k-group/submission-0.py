# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        group_prev = dummy

        while True:
            kth = self.get_kth(group_prev, k)

            if not kth:
                # if we are at the end
                # then we can just break since we do not need to reverse
                break
            
            group_next = kth.next
            prev, curr = kth.next, group_prev.next

            # Go until you hit the end of the
            # group
            while curr != group_next:
                # When you reverse you point the 
                # curr node back to the prev, basically
                # switch direction
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
        
        return dummy.next



    
    def get_kth(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        
        return curr