# Follow up for "Unique Paths":

# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.

# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.

# Note: m and n will be at most 100.

class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not len(obstacleGrid) or not len(obstacleGrid[0]):
            return 0

        cache = {}
        m, n = len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1

        return self.findPath(obstacleGrid, m, n, cache)

    def findPath(self, obstacleGrid, m, n, cache):
        if (m, n) in cache:
            return cache[(m, n)]
        elif m < 0 or n < 0 or obstacleGrid[m][n] == 1:
            return 0
        elif m == 0 and n == 0:
            return 1

        cache[(m, n)] = self.findPath(obstacleGrid, m - 1, n, cache) + self.findPath(obstacleGrid, m, n - 1, cache)

        return cache[(m, n)]
