class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    # 6:46
    def wordBreak(self, s, dict):
        if not s:
            return []

        output = []
        self.findWordBreak(s, dict, output, [])

        return output

    def findWordBreak(self, s, dict, output, temp):
        if not s:
            output.append(temp[:])
            return

        for i in range(1, len(s) + 1):
            if s[:i] in dict:
                temp.append(s[:i])
                self.findWordBreak(s[i:], dict, output, temp)
                temp.pop()

s = Solution()
print s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
