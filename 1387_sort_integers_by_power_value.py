from functools import lru_cache

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
    	ints = range(lo, hi+1)
    	return sorted(ints, key=getPower)[k-1]

@lru_cache
def getPower(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        transformed = n / 2
    if n % 2 == 1:
        transformed = (3 * n) + 1
    return getPower(transformed) + 1

s = Solution()
assert s.getKth(12, 15, 2) == 13
assert s.getKth(1, 1, 1) == 1
assert s.getKth(7, 11, 4) == 7
assert s.getKth(10, 20, 5) == 13
assert s.getKth(1, 1000, 777) == 570
