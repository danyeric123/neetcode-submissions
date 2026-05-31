"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        We need to do a mapping since nodes can be referenced again
        so we want to go the full path and then return it as neighbor 
        of new node. In essence, you will want to reuse the new created nodes
        again when other nodes have them as neighbors.
        Think of it like mapping is making sure we keep track of visited nodes
        """

        if not node: return node

        mapping = {}
        mapping[node] = Node(node.val)

        q = deque([node])

        while q:
            curr = q.popleft()

            for nei in curr.neighbors:
                if nei not in mapping:
                    mapping[nei] = Node(nei.val)
                    q.append(nei)
                mapping[curr].neighbors.append(mapping[nei])

        return mapping[node]