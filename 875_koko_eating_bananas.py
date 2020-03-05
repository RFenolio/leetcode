from math import ceil
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        low = 1
        high = max(piles)
        while low < high:
            mid = (low + high) // 2
            if sum((ceil(pile / mid) for pile in piles)) > H:
                low = mid + 1
            else:
                high = mid
        return low
            
s = Solution()

res1 = s.minEatingSpeed(piles=[3,6,7,11], H=8)
assert res1 == 4
res2 = s.minEatingSpeed(piles=[30,11,23,4,20], H=5)
assert res2 == 30
res3 = s.minEatingSpeed(piles=[30,11,23,4,20], H=6)
assert res3 == 23
res4 = s.minEatingSpeed(
	piles=[332484035, 524908576, 855865114, 632922376, 222257295, 690155293, 112677673, 679580077, 337406589, 290818316, 877337160, 901728858, 679284947, 688210097, 692137887, 718203285, 629455728, 941802184],
	H=823855818)
assert res4 == 14


