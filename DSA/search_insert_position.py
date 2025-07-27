# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        would_be_insert_index = 0
        
        for i in range(n):
            if nums[i] == target:
                return i
            elif nums[i] < target:
                would_be_insert_index = i + 1
        
        return would_be_insert_index
    
a = Solution()
print(a.searchInsert([1,3,5,6], 5))
print(a.searchInsert([1,3,5,6], 2))
print(a.searchInsert([1,3,5,6], 7))