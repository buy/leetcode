# Given a binary tree, flatten it to a linked list in-place.

# For example,
# Given

#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        self.flat(root)

    def flat(self, root):
        if not root:
            return None

        left = self.flat(root.left)
        right = self.flat(root.right)
        root.left = None
        root.right = None

        if left:
            root.right = left
        if right:
            self.getTail(root).right = right

        return root

    def getTail(self, root):
        while root.right:
            root = root.right

        return root
