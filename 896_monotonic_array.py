from itertools import tee
from typing import List

def pairwise(iterable):
    """
    implemented in python 3.10 as part of the standard library,
    but using a recipe from earlier versions.
    """
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return (all(a <= b for a, b in pairwise(nums)) or all(a >= b for a, b in pairwise(nums)))

s = Solution()
assert s.isMonotonic([1, 2, 3, 4, 4, 5, 5, 6]) == True
assert s.isMonotonic([1, 2, 3, 4, 4, 5, 5, 6][::-1]) == True
assert s.isMonotonic([1, 2, 3, 2, 1]) == False
assert s.isMonotonic([1, 2, 3, 4, 3, 4, 5, 6]) == False

