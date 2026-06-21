# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(
        self,
        root: Optional[TreeNode],
        left: int | float = float("-inf"),
        right: int | float = float("inf"),
    ) -> bool:
        # You need to pass down bounds (min/max values) 
        # to ensure each node falls within the valid range
        
        # the key that you might miss is that think in terms of
        # in order traversal and then optimize from there

        if not root:
            return True

        if not (left < root.val < right):
            return False

        return (
            self.isValidBST(root.left, left, root.val) and 
            self.isValidBST(root.right, root.val, right)
        )
