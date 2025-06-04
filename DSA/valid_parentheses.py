# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.

# Use stack to store opening bracket
# When encounter a closing bracket, check if top of stack was the opening for it
# If yes, pop it from the stack
# If no, return false

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i in bracket_map.values():
                stack.append(i)
            elif i in bracket_map:
                if not stack or stack[-1] != bracket_map[i]:
                    return False
                stack.pop()
            else:
                continue
        return not stack

answer = Solution()
print(answer.isValid("()[]{}"))
print(answer.isValid("([)]"))      
print(answer.isValid("{[]}"))      
print(answer.isValid("((("))       
print(answer.isValid("]"))         
