from itertools import permutations

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        all_permutations = permutations(nums)
        deduped = set(all_permutations)
        type_cast = sorted([list(item) for item in deduped])
        return type_cast