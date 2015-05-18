# Given an absolute path for a file (Unix-style), simplify it.

# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# click to show corner cases.

# Corner Cases:
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".


class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        stack = []
        path = filter(lambda x: x and x != '.', path.split('/'))
        for p in path:
            if p != '..':
                stack.append(p)
            elif stack:
                stack.pop()

        return '/' + '/'.join(stack)
