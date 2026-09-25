# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if not root:
            return root
        
        if root.val < key:
            # Then the key is in the right tree
            # and we need to have a new subtree
            # this is where the reassignment work goes
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # Need to move things around
            # Find the min from right subtree
            # so we have BST property kept
            curr = root.right

            while curr.left:
                curr = curr.left
            
            root.val = curr.val

            # Then you need to remove that min of the right tree
            root.right = self.deleteNode(root.right, root.val)
        
        return root