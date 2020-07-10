from math import factorial
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
    	return [calculate_cell(rowIndex, x) for x in range(1, rowIndex+2)]
        
def calculate_cell(n, x):
	return int(factorial(n) / (factorial(n - (x - 1)) * factorial(x - 1)))


s = Solution()
print(s.getRow(4))
# 𝑛!/ (𝑛−(𝑥−1))!(𝑥−1)!

