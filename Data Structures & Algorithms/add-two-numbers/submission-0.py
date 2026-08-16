# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_over = 0

        dummy = result = ListNode()
        curr1, curr2 = l1, l2

        while curr1 or curr2 or carry_over:

            # Handle where we are only dealing with
            # one of the two numbers (like one of 
            # them has an extra place)
            value1  = curr1.val if curr1 else 0
            value2 = curr2.val if curr2 else 0

            sum_ = value1 + value2 + carry_over

            carry_over = sum_ // 10
            value = sum_ % 10
            result.next = ListNode(value)

            # book keeping
            result = result.next
            curr1 = curr1.next if curr1 else curr1
            curr2 = curr2.next if curr2 else curr2

        return dummy.next