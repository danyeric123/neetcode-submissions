"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}

        if not head:
            return None
        
        curr = head

        while curr:
            # Get the mapping for all the nodes
            old_to_new[curr] = Node(x=curr.val)
            curr = curr.next
        
        # Then go through the linkages
        for node in old_to_new.keys():
            new_node = old_to_new[node]
            new_node.next = old_to_new[node.next] if node.next else None
            new_node.random = old_to_new[node.random] if node.random else None
        
        return old_to_new[head]