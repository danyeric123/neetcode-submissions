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
        
        :type root: TreeNode
        :rtype: str
        """

        res = []

        def dfs(node: Optional[TreeNode]):
            if not node:
                res.append("N")
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        return ",".join(res)
    

        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        node_vals = data.split(",")

        # to keep track of where you are in the list
        self.i = 0

        def dfs() -> TreeNode:
            if node_vals[self.i] == "N":
                self.i += 1
                return None
            
            node = TreeNode(int(node_vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            
            return node
        
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))