# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    # @param s, a string
    # @return an integer
    def romanToInt(self, s):
        ROMAN_INT = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                    'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                    'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        result = 0

        while s:
            if s[:2] in ROMAN_INT:
                result += ROMAN_INT[s[:2]]
                s = s[2:]
            else:
                result += ROMAN_INT[s[:1]]
                s = s[1:]

        return result
