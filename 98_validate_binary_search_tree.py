# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return is_valid_bst(root)[0]
        
def is_valid_bst(root: TreeNode):
    if root is None:
        return True, None, None
    if root.left is None and root.right is None:
        return True, root.val, root.val
    left_valid, left_min, left_max = is_valid_bst(root.left)
    right_valid, right_min, right_max = is_valid_bst(root.right)
    valid_children = left_valid and right_valid
    if (not valid_children 
        or (root.left is not None and left_max >= root.val)
        or (root.right is not None and right_min <= root.val)):
        return False, None, None
    return True, left_min or root.val, right_max or root.val
    