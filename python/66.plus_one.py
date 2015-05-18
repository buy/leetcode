# Given a non-negative number represented as an array of digits, plus one to the number.

# The digits are stored such that the most significant digit is at the head of the list.

class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        result, carry = [], 1
        for num in digits[::-1]:
            temp = num + carry
            carry = 1 if temp / 10 else 0
            result.append(temp % 10)

        if carry:
            result.append(carry)

        return result[::-1]
