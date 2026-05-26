# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        def same_tree(node1: Optional[TreeNode], node2:Optional[TreeNode]) -> bool:
            if not node1 or not node2: return node1 is node2

            return node1.val == node2.val and same_tree(node1.left, node2.left) and same_tree(node1.right, node2.right)

        if same_tree(root, subRoot): return True
        
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)