# Given a digit string, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below.

# NUM_CHAR = {0: None, 1: None, 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.

class Solution:
    def __init__(self):
        self.NUM_CHAR = [None, None, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    # @param digits, a string
    # @return a string[]
    def letterCombinations(self, digits):
        if not digits:
            return []

        digits = filter(lambda x: self.NUM_CHAR[int(x)] is not None, digits)
        output = []
        self.combine(digits, output, [])

        return output

    def combine(self, digits, output, temp, pos = 0):
        if pos == len(digits):
            output.append(''.join(temp))
            return

        for char in self.NUM_CHAR[int(digits[pos])]:
            temp.append(char)
            self.combine(digits, output, temp, pos + 1)
            temp.pop()
