# Given numRows, generate the first numRows of Pascal's triangle.

# For example, given numRows = 5,
# Return

# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution:
    BASE = 1
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows is 0:
            return []

        output = [[self.BASE]]
        for i in range(1, numRows):
            output.append([1])
            for j in range(1,i):
                output[i].append(output[i-1][j-1] + output[i-1][j])
            
            output[i].append(1)
        
        return output
