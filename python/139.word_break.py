# Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# For example, given
# s = "leetcode",
# dict = ["leet", "code"].

# Return true because "leetcode" can be segmented as "leet code".

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    # 6:16
    def wordBreak(self, s, dict):
        n = len(s)
        cache = [False] * (n + 1)

        for i in range(1, n + 1):
            for j in range(i):
                if s[j:i] in dict and (cache[j] or j == 0):
                    cache[i] = True

        return cache[n]

s = Solution()
print s.wordBreak("aaaaaaa", ["aaaa","aa"])
