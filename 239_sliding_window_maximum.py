from typing import List
from collections import deque
from math import inf

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_stack = []
        window = deque()
        for num in nums[:k]:
            window.append(num)
            if not max_stack or num >= max_stack[-1]:
                max_stack.append(num)
        res = [max_stack[-1]]
        for num in nums[k:]:
            # remove left item from window
            out = window.popleft()
            # if that was the previous max value, remove from max_stack
            if out == max_stack[-1]:
                max_stack.pop()
            #add the new num
            window.append(num)
            
            if num > max_stack[-1]:
                max_stack.append(num)
                print(max_stack)
            res.append(max_stack[-1])
        return res
s = Solution()


assert s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
# print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))

with open ("239_test_case.txt") as f:
    nums = [int(x) for x in f.read().strip().split(',')]
res = s.maxSlidingWindow(nums, 5000)
