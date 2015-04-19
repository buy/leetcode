# Given an integer, convert it to a roman numeral.

# Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    # @param num, an integer
    # @return a string
    def intToRoman(self, num):
        VALUE_ROMAN = {1000:"M", 900:"CM", 500:"D", 400:"CD",
                       100:"C", 90:"XC", 50:"L", 40:"XL",
                       10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}

        romanString = ''

        for v in sorted(VALUE_ROMAN.keys(), reverse = True):
            romanString += VALUE_ROMAN[v] * (num // v)
            num %= v

        return romanString

s = Solution()
print s.intToRoman(1439)
