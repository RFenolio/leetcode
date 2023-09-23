from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        nodes = [root]
        res = []
        while nodes:
            res.append([node.val for node in nodes])
            children = []
            for node in nodes:
                children.extend([node.left, node.right])
            