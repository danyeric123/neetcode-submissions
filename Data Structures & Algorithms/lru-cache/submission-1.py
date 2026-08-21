class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    """
    We can do this in two different ways:
    1. OrderedDict where we evict the last one, which dicts are now ordered
    2. LinkedList where we have to perform inserts and removals
    """
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = {}

        # we create dummy nodes to keep track of end and beginning
        # of linkedlist
        self.left, self.right = Node(0, 0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def _insert(self, node: Node) -> None:
        prev, nxt = self.right.prev, self.right
        # Shift everything to the right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    
    def _remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    

    def get(self, key: int) -> int:
        if key not in self._cache: 
            return -1
        
        # Move to end since it was used
        # by deleting and reinserting
        self._remove(self._cache[key])
        self._insert(self._cache[key])

        return self._cache[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            self._remove(self._cache[key])
        
        self._cache[key] = Node(key, value)
        self._insert(self._cache[key])

        # handle when we are over capacity
        if len(self._cache) > self._capacity:
            # Get the oldest by looking at left
            oldest_node = self.left.next
            self._remove(oldest_node)
            del self._cache[oldest_node.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)