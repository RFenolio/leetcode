from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        for idx, val in enumerate(nums):
            right -= val
            if left == right:
                return idx
            left += val
        return -1
    
s = Solution()
example1 = [1,7,3,6,5,6]
assert s.pivotIndex(example1) == 3
example2 = [1,2,3]
assert s.pivotIndex(example2) == -1
example3 = [2,1,-1]
assert s.pivotIndex(example3) == 0
