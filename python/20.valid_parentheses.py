# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution:
    # @param s, a string
    # @return a boolean
    def isValid(self, s):
        paren_map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []

        for p in s:
            if p in paren_map:
                stack.append(paren_map[p])
            else:
                if not stack or stack.pop() != p:
                    return False

        return not stack
