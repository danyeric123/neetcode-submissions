# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # inorder is root, left subtree, right subtree
        # preorder is left subtree, root, right subtree
        # so you will need to keep track of both since
        # you will know the root and left based off of them

        # We create a dictionary so we can easily reference
        # the other. This is instead of doing `.index()` to 
        # find the index of something

        value_to_pos = {value: index for index, value in enumerate(inorder)}

        def build_subtree(pre_start: int, in_start: int, subtree_size: int) -> Optional[TreeNode]:
            if subtree_size <= 0:
                return None
            
            # We know that the beginning of the preorder
            # is the root
            root_value = preorder[pre_start]

            # Then find location of it in inorder
            inorder_pos = value_to_pos[root_value]

            # Calculate size of left subtree
            left_subtree_size = inorder_pos - in_start

            # Recursively build left and right tree
            left_child = build_subtree(
                pre_start + 1, # move past root and you get left subtree
                in_start, # inorder will start the same since left subtree comes first
                left_subtree_size
            )

            right_child = build_subtree(
                pre_start + 1 + left_subtree_size, # Start after left subtree
                inorder_pos + 1, # right starts after root in inorder
                subtree_size - left_subtree_size - 1 # Remnaining nodes 
            )

            return TreeNode(root_value, left_child, right_child)



        
        return build_subtree(0,0,len(preorder))