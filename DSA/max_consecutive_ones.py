class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
       count = 0
       inner_count = 0

       for i in range(0, len(nums)):
           if nums[n] == 1:
               inner_count += 1
               if inner_count > count:
                   count = inner_count
           else:
               inner_count = 0
        
       return count

nums = [1,1,0,1,1,1]
a = Solution()
print(a.findMaxConsecutiveOnes(nums))