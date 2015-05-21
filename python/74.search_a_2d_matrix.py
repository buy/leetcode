# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,

# Consider the following matrix:

# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        if rows == 0:
            return False

        cols = len(matrix[0])
        i, j = 0, rows * cols - 1

        while i <= j:
            mid = (i + j) / 2
            num = matrix[mid / cols][mid % cols]
            if num == target:
                return True
            elif num > target:
                j = mid - 1
            else:
                i = mid + 1

        return False
