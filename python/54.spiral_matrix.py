# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# For example,
# Given the following matrix:

# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].

class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        result = []

        while matrix and matrix[0]:
            result += matrix.pop(0)

            if matrix and matrix[0]:
                result += [m.pop() for m in matrix]

            if matrix:
                result += matrix.pop()[::-1]

            if matrix and matrix[0]:
                result += [m.pop(0) for m in matrix[::-1]]

        return result
