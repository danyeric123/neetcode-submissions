# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(node: Optional[TreeNode]) -> tuple[bool, int]:
            if not node:
                return (True, 0)
            
            is_balanced_l, depth_l = depth(node.left)
            is_balanced_r, depth_r = depth(node.right)

            return (
                is_balanced_l and is_balanced_r and abs(depth_l - depth_r) in (0,1),
                1 + max(depth_l, depth_r)
            )
        
        balanced, _ = depth(root)
        return balanced