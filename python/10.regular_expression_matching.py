# Implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") -> false
# isMatch("aa","aa") -> true
# isMatch("aaa","aa") -> false
# isMatch("aa", "a*") -> true
# isMatch("aa", ".*") -> true
# isMatch("ab", ".*") -> true
# isMatch("aab", "c*a*b") -> true


class Solution:
    # @param s, a string
    # @param p, a string
    # @return a boolean
    def isMatch(self, s, p):
        if not s:
            return not p or len(p) == 2 and p[1] == '*'

        if not p:
            return not s

        if len(p) == 1:
            return len(s) == 1 and (s == p or p == '.')

        # next char is NOT *
        if p[1] != '*':
            return (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])
        else:
            # next char is *
            while s and (s[0] == p[0] or p[0] =='.'):
                if self.isMatch(s, p[2:]):
                    return True
                else:
                    s = s[1:]

            return self.isMatch(s, p[2:])


s = Solution()
print s.isMatch("a", "ab*")
