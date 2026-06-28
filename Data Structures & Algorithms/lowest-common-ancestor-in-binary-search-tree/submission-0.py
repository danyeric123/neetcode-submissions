# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q: return None

        if max(p.val, q.val) < root.val:
            # if they are both lower than the LCA 
            # must be in the left half
            return self.lowestCommonAncestor(root.left, p, q)
        
        if min(p.val, q.val) > root.val:
            # if both are larger than it
            # must be in the right half
            return self.lowestCommonAncestor(root.right, p, q)
        
        # Otherwise the root must be the LCA they share
        return root