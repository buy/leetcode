# Given a non-negative number represented as an array of digits, plus one to the number.

# The digits are stored such that the most significant digit is at the head of the list.

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        num = 0
        for d in digits:
            num *= 10
            num += d

        num += 1
        output = []

        while num:
            temp = num % 10
            num /= 10
            output.append(temp)

        return output[::-1]
