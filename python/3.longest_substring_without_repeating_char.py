# Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        charUsed = {}
        start = maxNum = 0
        
        for i in range(len(s)):
            if s[i] in charUsed and charUsed[s[i]] >= start:
                start = charUsed[s[i]] + 1
                charUsed[s[i]] = i
            else:
                charUsed[s[i]] = i
                maxNum = max(maxNum, i - start + 1)
        
        return maxNum
