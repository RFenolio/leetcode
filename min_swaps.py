
"""
Given an array of 1's and 0's, find the number of minimum adjacent swaps needed to group 1's and 0's together.  
1's or 0's can be on left or right side, whatever requires minimum swaps..

// Example 1
Input : [0,1,0,1]
Swaps needed : 0,1,0,1 -> 0,0,1,1 (1 swap from index 1 to index 2)

Solution: 1

// Example 2
Input : [1,0,1,0,0,0,0,1]
Swaps needed : 
1,0,1,0,0,0,0,1 -> 1,1,0,0,0,0,0,1 -> 1,1,0,0,0,0,1,0 -> 1,1,0,0,0,1,0,0 -> 1,1,0,0,1,0,0,0 -> 1,1,0,1,0,0,0,0 -> 1,1,1,0,0,0,0,0

Solution:  6
"""

def min_swaps(nums):
    l_total = 0
    r_total = 0
    l_count = 0
    r_count = 0
    for idx, num in enumerate(nums):
        if num == 1:
            l_total += idx - l_count
            l_count += 1
        else:
            r_total += idx - r_count
            r_count += 1
                
    return min(l_total, r_total)

print(min_swaps([1,0,1,0,0,0,0,1]))