# Given a string containing only digits, restore it by returning all possible valid IP address combinations.

# For example:
# Given "25525511135",

# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

import re

class Solution:
    # @param s, a string
    # @return a list of strings
    # 11:04
    def restoreIpAddresses(self, s):
        output, temp = [], []
        self.findSection(s, output, temp)
        
        return output

    def findSection(self, s, output, temp):
        if len(temp) == 4:
            if s:
                return
            else:
                output.append('.'.join(temp))
                return

        for i in range(1, 4):
            if i > len(s) or re.findall('^0\d+', s[:i]) or int(s[:i]) > 255:
                return
            temp.append(s[:i])
            self.findSection(s[i:], output, temp)
            temp.pop()

s = Solution()
print s.restoreIpAddresses('25525511155')
