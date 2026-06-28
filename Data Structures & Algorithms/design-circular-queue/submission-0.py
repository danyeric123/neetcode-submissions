class MyCircularQueue:

    def __init__(self, k: int):
        """
        :type k: int
        """
        # We need a way of keeping track of the head and tail
        # since that can change and popping off a list won't help
        # since ideally we want literal slots open before the head
        self.head = 0
        self.tail = 0

        # keeping track of the size and k is important
        # since those two things can drift apart
        self.size = 0
        self.k = k
        self.q = [None] * k

    def enQueue(self, value: int):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.size += 1
        self.q[self.tail] = value

        # To maintain circularity, we mod k
        self.tail = (self.tail + 1) % self.k
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False

        self.size -= 1

        # To maintain circularity, we mod k
        self.head = (self.head + 1) % self.k

        return True

    def Front(self):
        """
        :rtype: int
        """
        # The head will give us what is actually at the front, not the empty slots
        # after we dequeued
        return self.q[self.head] if not self.isEmpty() else -1

    def Rear(self):
        """
        :rtype: int
        """
        return self.q[self.tail - 1] if not self.isEmpty() else -1

    def isEmpty(self):
        """
        :rtype: bool
        """
        return True if self.size == 0 else False

    def isFull(self):
        """
        :rtype: bool
        """

        return True if self.size == self.k else False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
