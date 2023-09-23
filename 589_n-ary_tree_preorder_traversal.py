from collections import deque
from functools import reduce
from typing import List

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: Node) -> List[int]:
        """
        recursive solution
        """
        if not root:
            return []
        res = [root.val]
        return res + reduce(lambda a, b: a+b, (self.preorder(child) for child in root.children), [])\
        

    def preorder(self, root: Node) -> List[int]:
        """
        iterative solution
        """
        nodes = deque()
        if root:
            nodes.append(root)
        res = []
        while nodes:
            node = nodes.popleft()
            res.append(node.val)
            nodes.extendleft(list(reversed(node.children)))
        return res