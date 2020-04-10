from itertools import permutations
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return [list(item) for item in set(permutations(nums))]

s = Solution()
perms = s.permuteUnique
import dis
print(dis.dis(perms))