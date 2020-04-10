# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t is None:
            return ""
        l = self.tree2str(t.left)
        r = self.tree2str(t.right)
        if l or r:
            l = f"({l})"
        if r:
            r = f"({r})"
        return f"{t.val}{l}{r}"

s = Solution()
four = TreeNode(4)
two = TreeNode(2)
two.left = four
three = TreeNode(3)
one = TreeNode(1)
one.left = two
one.right = three

assert s.tree2str(one) == "1(2(4))(3)"

two.left = None
two.right = four

assert s.tree2str(one) =="1(2()(4))(3)"