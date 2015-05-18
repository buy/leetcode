# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# For example,
# Given n = 3,

# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        result = [[0] * n for i in range(n)]
        self.getMatrix(n, result)

        return result

    def getMatrix(self, n, result, offset = 0, cur = 1):
        if n % 2 == 0 and offset >= n / 2:
            return

        if n % 2 == 1 and offset > n / 2:
            return

        for i in range(offset, n - offset):
            result[offset][i] = cur
            cur += 1

        for i in range(offset + 1, n - offset):
            result[i][-offset - 1] = cur
            cur += 1

        for i in range(n - offset - 2, offset - 1, -1):
            result[n - offset - 1][i] = cur
            cur += 1

        for i in range(n - offset - 2, offset, -1):
            result[i][offset] = cur
            cur += 1

        self.getMatrix(n, result, offset + 1, cur)
