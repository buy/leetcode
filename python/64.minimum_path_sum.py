# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    # 1:40
    def minPathSum(self, grid):
        if not grid:
            return 0
        
        m, n = len(grid[0]), len(grid)
        dp = [[float('inf')] * (m + 1) for i in range(n + 1)]
        dp[0][1], dp[1][0] = 0, 0
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = grid[i-1][j-1] + min(dp[i-1][j], dp[i][j-1])
        
        return dp[n][m]

# recursive
class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        if not len(grid) or not len(grid[0]):
            return 0

        m, n, cache = len(grid) - 1, len(grid[0]) - 1, {}

        return self.findMinSum(grid, m, n, cache)

    def findMinSum(self, grid, m, n, cache):
        if (m, n) in cache:
            return cache[(m, n)]
        elif m < 0 or n < 0:
            return float('inf')
        elif m == 0 and n == 0:
            return grid[0][0]
        else:
            cache[(m, n)] = grid[m][n] + min(self.findMinSum(grid, m - 1, n, cache), self.findMinSum(grid, m, n - 1, cache))

            return cache[(m, n)]
