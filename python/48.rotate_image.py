# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

# Follow up:
# Could you do this in-place?

# /*
#  * clockwise rotate
#  * first reverse up to down, then swap the symmetry 
#  * 1 2 3     7 8 9     7 4 1
#  * 4 5 6  => 4 5 6  => 8 5 2
#  * 7 8 9     1 2 3     9 6 3
# */

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# /*
#  * anticlockwise rotate
#  * first reverse left to right, then swap the symmetry
#  * 1 2 3     3 2 1     3 6 9
#  * 4 5 6  => 6 5 4  => 2 5 8
#  * 7 8 9     9 8 7     1 4 7
# */
