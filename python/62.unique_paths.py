# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        cache = {}
        return self.findPath(m, n, cache)

    def findPath(self, m, n, cache):
        if (m, n) in cache:
            return cache[(m, n)]
        elif m == 1 or n == 1:
            return 1

        cache[(m, n)] = self.findPath(m - 1, n, cache) + self.findPath(m, n - 1, cache)

        return cache[(m, n)]
