# Given an integer x, return true if x is a -palindrome-, and false otherwise.

# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        convert_str = str(x)
        rev_str = ""
        for i in range(len(convert_str)-1, -1, -1):
            rev_str += convert_str[i]

        if rev_str != convert_str:
            return False

        return True
    
a = Solution()
print(a.isPalindrome(-121))
print(a.isPalindrome(121))
print(a.isPalindrome(12))