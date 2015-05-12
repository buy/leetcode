# Given an array of strings, return all groups of strings that are anagrams.

# Note: All inputs will be in lower-case.

class Solution:
    # @param {string[]} strs
    # @return {string[]}
    # 8:06
    def anagrams(self, strs):
        result, output = {}, []
        for str in strs:
            key = ''.join(sorted(str))
            if key in result:
                result[key].append(str)
            else:
                result[key] = [str]

        for re in result.values():
            if len(re) > 1:
                output += re

        return output
