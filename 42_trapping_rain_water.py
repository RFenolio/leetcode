from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        highest_left = []
        highest_right = []
        left_max = 0
        right_max = 0
        for val in height:
            if val > left_max:
                left_max = val
            highest_left.append(left_max)
        for val in height[::-1]:
            if val > right_max:
                right_max = val
            highest_right.append(right_max)
        peaks = zip(highest_left[::-1], highest_right, height)
        total_water = sum(min(l, r) - h for l, r, h in peaks)
        return total_water

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))