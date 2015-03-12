# Implement int sqrt(int x).

# Compute and return the square root of x.

class Solution:
    # @param x, an integer
    # @return an integer
    # 8:54
    def sqrt(self, x):
        i, j = 0, x / 2 + 1
        
        while i <= j:
            mid = (i + j) / 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                j = mid - 1
            else:
                i = mid + 1

        return (i + j) / 2
