# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

# Your algorithm should run in O(n) complexity.

class Solution:
    # @param num, a list of integer
    # @return an integer
    # 11:19
    def longestConsecutive(self, num):
        if not num:
            return 0

        num = sorted(list(set(num)))
        curLen, maxLen = 1, 1
        for i in range(1, len(num)):
            if num[i] - num[i-1] == 1:
                curLen += 1
            else:
                if curLen > maxLen:
                    maxLen = curLen
                curLen = 1

        if curLen > maxLen:
            maxLen = curLen

        return maxLen
