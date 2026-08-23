# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # From a basic perspective, you could simply do an in-order
        # traversal and get the kth element that way

        # BUT you could also do a recursive DFS where you keep track of
        # how many you have seen (with an in order traversal)

        self.res = 0
        self.num_seen = 0

        def in_order(node: Optional[TreeNode]) -> None:
            if not node:
                return
            
            # Go left
            in_order(node.left)

            # visit this node
            self.num_seen += 1
            if self.num_seen == k:
                self.res = node.val
                return
            
            # then go right
            in_order(node.right)
            
        
        in_order(root)
        return self.res