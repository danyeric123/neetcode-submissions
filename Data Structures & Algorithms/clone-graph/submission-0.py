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

        def dfs(node: 'Node')->'Node':
            mapping[node] = Node(node.val)

            for neigh in node.neighbors:
                if neigh not in mapping: dfs(neigh)
                mapping[node].neighbors.append(mapping[neigh])
        
        dfs(node)

        return mapping[node]