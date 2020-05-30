class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        l = len(s)
        left = s[:l//2]
        right = s[(l//2) + (l % 2):][::-1]
        return left == right

s = Solution()
assert s.isPalindrome("aa") == True
assert s.isPalindrome("A man, a plan, a canal: Panama") == True
assert s.isPalindrome("race a car") == False
assert s.ispalindrome("") == True