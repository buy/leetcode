# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

# An example is the root-to-leaf path 1->2->3 which represents the number 123.

# Find the total sum of all root-to-leaf numbers.

# For example,

#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.

# Return the sum = 12 + 13 = 25.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    # 1:47
    def sumNumbers(self, root, path = 0):
        if not root:
            return path

        path = path * 10 + root.val
        left = self.sumNumbers(root.left, path)
        right = self.sumNumbers(root.right, path)

        if left == path:
            return right
        elif right == path:
            return left
        else:
            return left + right
