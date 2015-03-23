class Solution:
    # @param s, a string
    # @return an integer
    # 5:31
    def __init__(self):
        self.numMinCut = float('inf')

    def minCut(self, s):
        if not s:
            return 0

        self.findMinCut(s, [])
        return self.numMinCut

    def findMinCut(self, s, temp):
        if not s:
            numCut = len(temp) - 1
            if numCut < self.numMinCut:
                self.numMinCut = numCut
            return

        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                temp.append(s[:i])
                self.findMinCut(s[i:], temp)
                temp.pop()

    def isPalindrome(self, s):
        return s == s[::-1]

s = Solution()
print s.minCut('ababababababababab')
