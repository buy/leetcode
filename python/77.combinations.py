# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# For example,
# If n = 4 and k = 2, a solution is:

# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

class Solution:
    # @return a list of lists of integers
    # 9:14
    def __init__(self):
        self.output = []

    def combine(self, n, k, pos=0, temp=None):
        temp = temp or []
        
        if len(temp) == k:
            self.output.append(temp[:])
            return

        for i in range(pos, n):
            temp.append(i+1)
            self.combine(n, k, i+1, temp)
            temp.pop()
        
        return self.output
