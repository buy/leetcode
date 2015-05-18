# The set [1,2,3,…,n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

# Note: Given n will be between 1 and 9 inclusive.

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        nums, result = [i + 1 for i in range(n)], ''

        while n > 0:
            totalCount = math.factorial(n - 1)
            index = (k - 1) / totalCount
            result += str(nums.pop(index))
            n -= 1
            k %= totalCount

        return result
