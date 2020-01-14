from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        current_max = 0
        while i >= 0:
            if nums[i] < current_max:
                break
            current_max = max(nums[i], current_max)
            i -= 1
        if i == -1:
            nums.sort()
        else:
            for j in range(len(nums) - 1, i, -1):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
            nums[i+1:] = sorted(nums[i+1:])