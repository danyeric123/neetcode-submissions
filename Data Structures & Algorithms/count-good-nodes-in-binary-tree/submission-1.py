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
        
        num_good = 0

        q = deque([(root, root.val)])

        while q:
            node, max_val = q.popleft()

            if node.val >= max_val:
                num_good += 1
            
            max_val = max(max_val, node.val)

            if node.left:
                q.append(
                    (node.left, max_val)
                )
            
            if node.right:
                q.append(
                    (node.right, max_val)
                )
            
        return num_good