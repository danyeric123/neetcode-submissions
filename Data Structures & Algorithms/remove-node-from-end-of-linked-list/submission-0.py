# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = fast = slow = ListNode(0,next=head)

        # We move the fast so that it is 
        # n nodes ahead so that when we get
        # to the end with fast, we moved N - n places
        # meaning we got to the n-th place
        for _ in range(n):
            fast = fast.next
        
        # Then we move both of them
        # until we hit the end
        
        # The idea is that fast tells
        # us when we hit the end
        # and slow is moved to right
        # before N
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummy.next