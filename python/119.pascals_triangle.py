# Given an index k, return the kth row of the Pascal's triangle.

# For example, given k = 3,
# Return [1,3,3,1].

# Note:
# Could you optimize your algorithm to use only O(k) extra space?

class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        result = [1]

        for i in range(1, rowIndex + 1):
            cur = []
            for j in range(1, i):
                cur.append(result[j - 1] + result[j])
            result = [1] + cur + [1]

        return result
