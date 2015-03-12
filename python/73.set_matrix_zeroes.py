# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
# Follow up:
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

class Solution:
    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything, MODIFY matrix IN PLACE.
    # 12:35
    def setZeroes(self, matrix):
        zeroRows = set()
        zeroCols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroRows.add(i)
                    zeroCols.add(j)

        for row in zeroRows:
            matrix[row][:] = map(lambda x:0, matrix[row])

        for i in range(len(matrix)):
            for col in zeroCols:
                matrix[i][col] = 0
