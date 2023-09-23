from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        total = 1 if any(num % 2 == 1 for num in counts.values()) else 0
        for val in counts.values():
            total += (val // 2) * 2
        return total

s = Solution()
e1 = "abccccdd"
e2 = "a"
assert s.longestPalindrome(e1) == 7
assert s.longestPalindrome(e2) == 1