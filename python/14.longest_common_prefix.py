# Write a function to find the longest common prefix string amongst an array of strings.

class Solution:
    # @param strs, a string[]
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''

        return reduce(self.getLCP, strs)

    def getLCP(self, x, y):
        n, lcp = min(len(x), len(y)), ''

        for i in range(n):
            if x[i] != y[i]:
                break
            else:
                lcp += x[i]

        return lcp
