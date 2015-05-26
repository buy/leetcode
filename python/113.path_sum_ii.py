# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    def pathSum(self, root, sum):
        result = []
        self.findPath(root, sum, result, [])

        return result

    def findPath(self, root, sum, result, temp):
        if not root:
            return

        temp.append(root.val)
        if sum == root.val and not root.left and not root.right:
            result.append(temp)
            return

        sum -= root.val
        self.findPath(root.left, sum, result, temp[:])
        self.findPath(root.right, sum, result, temp[:])
