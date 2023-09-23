class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        idx = t.find(s[0])
        if idx == -1:
            return False
        else:
            return self.isSubsequence(s[1:], t[idx+1:])


s = Solution()
example1 = ('abc', 'ahbgdc')
example2 = ('axc', 'ahbgdc')
assert s.isSubsequence(*example1) == True
assert s.isSubsequence(*example2) == False