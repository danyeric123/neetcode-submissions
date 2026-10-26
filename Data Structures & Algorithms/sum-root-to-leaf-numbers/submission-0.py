# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        
        def dfs(node: TreeNode | None, curr_total: int) -> int:
            if not node: return 0

            # Move everything one place over
            curr_total = curr_total * 10 + node.val

            if not node.left and not node.right:
                return curr_total
            
            # Add the two branches but pass the amount we have so far
            # since it will be offset and then the rest of the subtree 
            # will be added
            return dfs(node.left, curr_total) + dfs(node.right, curr_total)
        
        return dfs(root, 0)