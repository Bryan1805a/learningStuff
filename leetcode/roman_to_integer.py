# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together.
# 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

class Solution:
    def romanToInt(self, s: str) -> int:
        this_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        answer = 0
        prev_value = 0

        for char in reversed(s):
            value = this_dict[char]
            if value < prev_value:
                answer -= value
            else:
                answer += value
            prev_value = value
        return answer