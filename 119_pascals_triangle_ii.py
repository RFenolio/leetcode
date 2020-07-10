from math import factorial
from typing import List

# math based solution
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
    	return [calculate_cell(rowIndex, x) for x in range(1, rowIndex+2)]
        
def calculate_cell(n, x):
	return int(factorial(n) / (factorial(n - (x - 1)) * factorial(x - 1)))

# recursive solution
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
    	if rowIndex == 0:
    		return [1]
    	else:
    		prev = self.getRow(rowIndex - 1)
    		return [1] + list(sum(prev[idx: idx+2]) for idx, val in enumerate(prev))
    		