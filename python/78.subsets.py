# Given a set of distinct integers, nums, return all possible subsets.

# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If nums = [1,2,3], a solution is:

# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        result = []
        self.getCombination(n, k, result, [])

        return result

    def getCombination(self, n, k, result, temp, start = 1):
        if len(temp) == k:
            result.append(temp[:])
            return

        for i in range(start, n + 1):
            temp.append(i)
            self.getCombination(n, k, result, temp, i + 1)
            temp.pop()
