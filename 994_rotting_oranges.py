from itertools import chain
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not any(orange == 2 for orange in chain(*grid)):
        	return -1
        while not any (orange == 2 for orange in chain(*grid)):

grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[1,1,1],[1,1,1],[1,1,1]]
print(not any(orange == 2 for orange in chain(*grid)))