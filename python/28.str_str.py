# Implement strStr().

# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        n = len(needle)

        for i in range(len(haystack) - n + 1):
            if haystack[i:i+n] == needle:
                return i

        return -1
