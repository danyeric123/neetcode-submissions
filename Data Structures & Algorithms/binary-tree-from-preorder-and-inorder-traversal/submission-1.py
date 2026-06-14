# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Create a dictionary mapping values to their positions in inorder traversal
        # This allows O(1) lookup of a value's position in inorder traversal
        # Having both tells us how to divide each of the orders, and this is faster
        # since we do not need to search the lists

        value_to_position = {value: index for index, value in enumerate(inorder)}

        def build_subtree(pre_start: int, in_start: int, subtree_size: int) -> Optional[TreeNode]:
            """
            Recursively builds a subtree using portions of preorder and inorder traversals.
            
            Args:
                pre_start: Starting index in preorder traversal
                in_start: Starting index in inorder traversal
                subtree_size: Number of nodes in current subtree
            
            Returns:
                Root node of the constructed subtree
            """
            # Base case: if subtree is empty
            if subtree_size <= 0:
                return None
                
            # Root value is always first in preorder traversal
            root_value = preorder[pre_start]
            
            # Find position of root value in inorder traversal
            inorder_root_pos = value_to_position[root_value]
            
            # Calculate size of left subtree
            left_subtree_size = inorder_root_pos - in_start
            
            # Recursively build left and right subtrees
            left_child = build_subtree(
                pre_start + 1,  # Move past root in preorder
                in_start,       # Left subtree starts at in_start
                left_subtree_size  # Size of left subtree
            )
            
            right_child = build_subtree(
                pre_start + 1 + left_subtree_size,  # Skip root and left subtree in preorder
                inorder_root_pos + 1,               # Right subtree starts after root in inorder
                subtree_size - left_subtree_size - 1  # Remaining nodes form right subtree
            )
            
            # Create and return the root node with its children
            return TreeNode(root_value, left_child, right_child)
        
        return build_subtree(0, 0, len(preorder))