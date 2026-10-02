class ListNode:
    def __init__(
        self, 
        val: int, 
        nxt: "ListNode | None" = None, 
    ):
        self.val, self.next = val, nxt

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.k = k
        self.left = ListNode(0)
        # left will be a dummy node 
        # while right will be the value
        self.right = self.left

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        
        # Create a new node
        curr = ListNode(value)
        
        if self.isEmpty():
            self.left.next = curr
            self.right = curr
        else:
            # Need the right.next to be curr
            # to make sure we do not get null
            # in next.next in dequeue
            self.right.next = curr
            self.right = curr

        self.size += 1
        self.k -= 1
        return True

    def deQueue(self) -> bool:

        if self.isEmpty(): return False

        self.left.next = self.left.next.next

        # if this is the last node
        if self.left.next is None:
            self.right = self.left

        self.size -=1
        self.k +=1
        return True
        

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.left.next.val
        

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.right.val
        

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