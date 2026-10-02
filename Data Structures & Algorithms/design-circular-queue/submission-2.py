class ListNode:
    def __init__(
        self, 
        val: int, 
        nxt: "ListNode | None" = None, 
        prev:  "ListNode | None" = None
    ):
        self.val, self.next, self.prev = val, nxt, prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.k = k
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        
        # Create a new node
        curr = ListNode(value, self.right, self.right.prev)
        self.right.prev.next = curr
        self.right.prev = curr
        self.size += 1
        self.k -= 1
        return True

    def deQueue(self) -> bool:

        if self.isEmpty(): return False

        # Connect the left to the one after
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.size -=1
        self.k +=1
        return True
        

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.left.next.val
        

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.right.prev.val
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.k == 0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()