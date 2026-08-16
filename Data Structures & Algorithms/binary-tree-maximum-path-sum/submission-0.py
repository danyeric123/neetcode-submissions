# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        The key here is either split or not. We either split once or not at all
        since we can only traverse once.
        """

        self.res = root.val

        # return the max without split
        # but calculate the split against max
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # We do not need to include children
            # so any negatives will be excluded
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)

            # Compute the max with split vs current res
            self.res = max(self.res, node.val + left_max + right_max)

            # return the value without the split since the caller will be 
            # implementing the split
            return node.val + max(left_max, right_max)
        
        dfs(root)

        return self.res