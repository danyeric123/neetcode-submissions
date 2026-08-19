# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        With every tree we can do DFS (or BFS). The idea is 
        we need to keep track of the max value we have seen
        so far and then pass that as we go through the tree
        and as we pass if we keep track if this would be a 
        good node
        """
        
        def dfs(node: Optional[TreeNode], max_val: int) -> int:
            if not node: return 0

            num_good = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)

            num_good += dfs(node.left, max_val)
            num_good += dfs(node.right, max_val)

            return num_good
        
        return dfs(root, root.val)