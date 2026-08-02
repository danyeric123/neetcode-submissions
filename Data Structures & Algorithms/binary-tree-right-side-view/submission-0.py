# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # We want to do a BFS so that we can grab the 
        # rightmost
        if not root: return []

        side = []

        q = deque([root])

        while q:
            level = []

            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # Append the very last of that level
            side.append(level[-1])
        
        return side