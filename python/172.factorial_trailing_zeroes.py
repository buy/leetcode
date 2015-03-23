# Given an integer n, return the number of trailing zeroes in n!.

# Note: Your solution should be in logarithmic time complexity.


class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        factor, count = 5, 0
        
        while True:
            curCount = n // factor
            if not curCount:
                break
            
            count += curCount
            factor *= 5

        return count
