# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.

        Serializing is easy since all you need is DFS
        and we just need to decide what order traversal for
        both

        or BFS with level ordering
        
        :type root: TreeNode
        :rtype: str
        """

        res = []

        if not root:
            return "N"
        
        q = deque([root])

        while q:
            node = q.popleft()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        
        return ",".join(res)
    

        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        node_vals = data.split(",")

        # to keep track of where you are in the list
        i = 0

        if node_vals[i] == "N":
            return None
        
        root = TreeNode(int(node_vals[i]))
        q = deque([root])
        i += 1
        while q:
            node = q.popleft()

            if node_vals[i] != "N":
                node.left = TreeNode(int(node_vals[i]))
                q.append(node.left)
            i += 1
            if node_vals[i] != "N":
                node.right = TreeNode(int(node_vals[i]))
                q.append(node.right)
            i += 1
        
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))