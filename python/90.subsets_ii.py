# Given a collection of integers that might contain duplicates, S, return all possible subsets.

# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,2], a solution is:

# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    # 1:02
    def __init__(self):
        self.output = []

    def subsetsWithDup(self, S, pos = 0, temp = None):
        temp = temp or []
        S.sort()

        if temp not in self.output:
          self.output.append(temp[:])

        for i in range(pos, len(S)):
            temp.append(S[i])
            self.subsetsWithDup(S, i+1, temp)
            temp.pop()

        return self.output

s = Solution()
print s.subsetsWithDup([1,2,2])
