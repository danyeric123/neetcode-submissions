# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        # First you search for the beginning and end
        # then reverse it

        if not head: return None

        dummy = ListNode(0, head)
        left_prev, curr = dummy, head

        # grab right before left starts
        for _ in range(left - 1):
            left_prev, curr = curr, curr.next
        
        prev = None
        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev, curr = curr, next_node
        
        # Move the beginning of our reverse
        # to point to right
        left_prev.next.next = curr
        # move the left previous to point to
        # end of our reverse
        left_prev.next = prev

        return dummy.next