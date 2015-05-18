# Given two binary strings, return their sum (also a binary string).

# For example,
# a = "11"
# b = "1"
# Return "100".

class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        i, m, n, result, carry = 1, len(a), len(b), [], 0
        while i <= m or i <= n:
            temp = carry
            if i <= m:
                temp += int(a[-i])
            if i <= n:
                temp += int(b[-i])

            carry = temp / 2
            result.append(str(temp % 2))
            i += 1

        if carry:
            result.append(str(carry))

        return ''.join(result[::-1])


class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        return '{0:b}'.format(int(a, 2) + int(b, 2))
